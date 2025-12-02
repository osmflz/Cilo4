from ultralytics import YOLO

# Pretrained model yükle (s, n, m fark etmez: s hızlı ve yeterli)
model = YOLO("yolov8s.pt")

DATA_PATH = "wheel_dataset/data.yaml"

model.train(
    data=DATA_PATH,
    epochs=50,
    imgsz=640,
    batch=8,
    workers=4,
)