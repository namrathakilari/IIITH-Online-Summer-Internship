from ultralytics import YOLO

model = YOLO("yolo26n.pt")

model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=384,
    batch=8,
    project="runs/train",
    name="cars_trucks"
)