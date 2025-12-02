pip install onnx onnxruntime


from ultralytics import YOLO

# PyTorch modelini yükle
model = YOLO("yolov8s.pt")

# ONNX olarak kaydet
model.export(format="onnx")


import onnxruntime as ort
import cv2
import numpy as np

# ONNX modelini yükle
session = ort.InferenceSession("yolov8s.onnx")

# Kamera aç
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Frame'i model giriş boyutuna getir
    img = cv2.resize(frame, (640, 640))
    img = img.transpose(2,0,1)  # HWC -> CHW
    img = img[np.newaxis, :, :, :].astype(np.float32) / 255.0

    outputs = session.run(None, {session.get_inputs()[0].name: img})

    # outputs içinden kutuları alıp çizebilirsin
    # (Ultralytics plot gibi otomatik değil, kendin parse etmen gerekir)

    cv2.imshow("YOLOv8 ONNX", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()