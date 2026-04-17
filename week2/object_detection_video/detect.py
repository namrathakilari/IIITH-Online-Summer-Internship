from ultralytics import YOLO

# 1. Load the model (It will use the yolo26n.pt file in your folder)
model = YOLO('yolo26n.pt') 

# 2. Run detection on your video
# This will save the output in a folder named 'runs'
results = model.predict(source='raw_video.mp4', save=True)

# 3. Print the results to the terminal to verify
for result in results:
    print(result.boxes)