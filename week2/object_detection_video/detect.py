from ultralytics import YOLO
import os

model = YOLO("yolo26n.pt")  # downloads pretrained weights automatically

input_dir = "frames"
output_dir = "annotated_frames"
os.makedirs(output_dir, exist_ok=True)

frames = sorted([f for f in os.listdir(input_dir) if f.endswith(".jpg")])
total = len(frames)

for i, fname in enumerate(frames):
    input_path = os.path.join(input_dir, fname)
    results = model(input_path, verbose=False)
    results[0].save(filename=os.path.join(output_dir, fname))
    if i % 100 == 0:
        print(f"Processed {i}/{total} frames...")

print("Done! All frames annotated.")