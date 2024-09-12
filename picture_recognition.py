import cv2
from fer import FER
import numpy as np

# Initialize the FER detector
detector = FER()

# Load the image
image_path = '/images/kumar.jpeg'
image = cv2.imread(image_path)

# Detect emotions in the image
emotions = detector.detect_emotions(image)

# Draw rectangles and labels on the image
for emotion in emotions:
    (x, y, w, h) = emotion['box']
    emotion_text = max(emotion['emotions'], key=emotion['emotions'].get)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(image, emotion_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the resulting image
cv2.imshow('Emotion Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()