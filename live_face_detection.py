import cv2
from fer import FER
import numpy as np
import tensorflow as tf

detector = FER()

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions in the frame
    emotions = detector.detect_emotions(frame)
    for emotion in emotions:
        # Get the emotion with the highest score
        (x, y, w, h) = emotion['box']
        emotion_text = max(emotion['emotions'], key=emotion['emotions'].get)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Emotion Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()