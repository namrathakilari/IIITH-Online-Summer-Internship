import os, shutil

frames_dir = "frames"
all_frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

total = len(all_frames)
train_end = int(total * 0.65)
val_end   = int(total * 0.85)

train = all_frames[:train_end]
val   = all_frames[train_end:val_end]
test  = all_frames[val_end:]

for f in train:
    shutil.copy(os.path.join(frames_dir, f), os.path.join("dataset/train/images", f))
for f in val:
    shutil.copy(os.path.join(frames_dir, f), os.path.join("dataset/val/images", f))
for f in test:
    shutil.copy(os.path.join(frames_dir, f), os.path.join("dataset/test/images", f))

print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}")