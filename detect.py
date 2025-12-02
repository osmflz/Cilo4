from ultralytics import YOLO
import cv2

# Modeli yükle
model = YOLO("/home/pi/yolov8s.pt")

# Kamera aç
cap = cv2.VideoCapture(0)  # HQ kamera default 0 olabilir

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO tespiti
    results = model(frame)

    # Sonuçları çiz
    annotated_frame = results[0].plot()  # plot() görüntüyü annotate eder

    cv2.imshow("YOLOv8 Live", annotated_frame)

    # Çıkış için q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()