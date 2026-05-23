import os, shutil, re

# ── CONFIGURE THESE ──────────────────────────────────────────────────────────
LABELS_ZIP_FOLDER = "ls_export" # folder where you extracted the zip
TRAIN_LABELS_OUT  = "dataset/train/labels"
VAL_LABELS_OUT    = "dataset/val/labels"

# Frames 0001-0031 → train  (31 images)
# Frames 0032-0040 → val    (9 images)
TRAIN_MAX_FRAME = 31
# ─────────────────────────────────────────────────────────────────────────────

os.makedirs(TRAIN_LABELS_OUT, exist_ok=True)
os.makedirs(VAL_LABELS_OUT,   exist_ok=True)

train_count = 0
val_count   = 0
skipped     = 0

for fname in os.listdir(LABELS_ZIP_FOLDER):
    if not fname.endswith(".txt"):
        continue

    # Extract frame number from filename like: 07015937-frame_0004.txt
    match = re.search(r"frame_(\d+)\.txt$", fname)
    if not match:
        print(f"  SKIP (no frame number): {fname}")
        skipped += 1
        continue

    frame_num = int(match.group(1))
    src = os.path.join(LABELS_ZIP_FOLDER, fname)

    # New filename matches the original image name: frame_0004.txt
    new_name = f"frame_{frame_num:04d}.txt"

    if frame_num <= TRAIN_MAX_FRAME:
        dst = os.path.join(TRAIN_LABELS_OUT, new_name)
        shutil.copy(src, dst)
        train_count += 1
    else:
        dst = os.path.join(VAL_LABELS_OUT, new_name)
        shutil.copy(src, dst)
        val_count += 1

print(f"\nDone!")
print(f"  Train labels: {train_count}  →  {TRAIN_LABELS_OUT}")
print(f"  Val labels:   {val_count}    →  {VAL_LABELS_OUT}")
if skipped:
    print(f"  Skipped:      {skipped}")
print(f"\nVerify counts match your images:")
print(f"  (dir dataset\\train\\labels).Count  →  should be {train_count}")
print(f"  (dir dataset\\val\\labels).Count    →  should be {val_count}")
