from ultralytics import YOLO
import torch

device = "mps" if torch.backends.mps.is_available() else "cpu"
print("Using:", device)

model = YOLO("yolov8s.pt")

model.train(
    data="datasets/wheel_dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,           # M1 Pro için ideal
    device=device,     # GPU kullanımı
)