from ultralytics import YOLO

model = YOLO("my_cars_trucks.pt")

model.predict(
    source="dataset/test/images/",
    save=True,
    project="runs/detect",
    name="results"
)