import os
import sys
import time
import cv2
from fer.fer import FER
import pandas as pd

def main():

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    detector = FER(mtcnn=True)

    logs = []
    last_logged_time = 0

    window_name = "Live Emotion Detection"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    print("--- Emotion Detection Started ---")
    print("Press 'Q' while clicking on the camera window to quit and save report.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame from camera.")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            try:

                results = detector.detect_emotions(rgb_frame)

                if results:

                    face = results[0]
                    x, y, w, h = face["box"]
                    emotions = face["emotions"]

                    dominant_emotion = max(emotions, key=emotions.get)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    text = f"{dominant_emotion.upper()} ({int(emotions[dominant_emotion]*100)}%)"
                    cv2.putText(
                        frame,
                        text,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )

                    current_time = time.time()
                    if current_time - last_logged_time >= 1.0:
                        logs.append(
                            {
                                "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                                "Dominant Emotion": dominant_emotion,
                                "Happy": round(emotions.get("happy", 0), 3),
                                "Sad": round(emotions.get("sad", 0), 3),
                                "Angry": round(emotions.get("angry", 0), 3),
                                "Fear": round(emotions.get("fear", 0), 3),
                                "Surprise": round(emotions.get("surprise", 0), 3),
                                "Disgust": round(emotions.get("disgust", 0), 3),
                                "Neutral": round(emotions.get("neutral", 0), 3),
                            }
                        )
                        last_logged_time = current_time

                else:

                    cv2.putText(
                        frame,
                        "Searching for face...",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2,
                    )

            except Exception as e:
                print(f"Detection Error: {e}")

            cv2.imshow(window_name, frame)


            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or cv2.getWindowProperty(
                window_name, cv2.WND_PROP_VISIBLE
            ) < 1:
                break

    finally:

        cap.release()
        cv2.destroyAllWindows()


    if logs:
        try:
            df = pd.DataFrame(logs)

            if "__file__" in globals():
                script_dir = os.path.dirname(os.path.abspath(__file__))
            else:
                script_dir = os.getcwd() 

            file_name = os.path.join(
                script_dir, f"Emotion_Report_{int(time.time())}.xlsx"
            )

            df.to_excel(file_name, index=False, engine="openpyxl")

            print("\n" + "=" * 40)
            print(" REPORT GENERATED SUCCESSFULLY")
            print(f" Saved Location: {file_name}")
            print("=" * 40)

        except Exception as e:
            print(f"\nExcel Save Error: {e}")
    else:
        print("\nNo emotion data recorded. Report skipped.")

if __name__ == "__main__":
    main()