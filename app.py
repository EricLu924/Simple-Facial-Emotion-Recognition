import cv2
import numpy as np
from keras.models import load_model

# 載入模型(Load the model)
model = load_model('emotion_model.h5')

# 定義情緒類別(Define emotion categories)
emotion_labels = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise', 'neutral']

# 開啟鏡頭(Turn on the camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 將彩色圖像轉為灰階(Convert color images to grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 偵測人臉(Detect faces)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces: 
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_gray_resized = cv2.resize(roi_gray, (48, 48)).reshape(1, 48, 48, 1) / 255.0
        
        # 進行辨識(Perform recognition)
        emotion_prediction = model.predict(roi_gray_resized)
        # 確認 numpy 函數的使用(Verify the use of numpy functions)
        max_index = np.argmax(emotion_prediction[0])  
        predicted_emotion = emotion_labels[max_index]

        # 顯示辨識結果(Display recognition results)
        cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 顯示即時影像(Display real-time video)
    cv2.imshow('Facial Emotion Recognition', frame) 