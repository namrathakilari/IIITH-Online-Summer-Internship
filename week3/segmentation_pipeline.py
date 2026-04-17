import os
import subprocess
from ultralytics import YOLO

# 1. Setup Absolute Paths (This fixes the FileNotFoundError)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FRAMES = os.path.join(BASE_DIR, "week1", "task2", "frames")
AUDIO_FILE = os.path.join(BASE_DIR, "week1", "task3", "clipped_audio.mp3") 
OUTPUT_VIDEO = "semantic_segmented_output.mp4"

def main():
    # Verify the path exists before starting
    if not os.path.exists(INPUT_FRAMES):
        print(f"Error: Could not find frames at {INPUT_FRAMES}")
        return

    # 2. Initialize YOLO26 Segmentation
    print("--- Loading YOLO26 Nano Segmentation Model ---")
    model = YOLO("yolo26n-seg.pt") 
    
    # 3. Run Segmentation
    print("--- Starting Pixel-wise Segmentation ---")
    model.predict(
        source=INPUT_FRAMES, 
        save=True, 
        project="runs/segment", 
        name="internship_seg",
        exist_ok=True 
    )
    
    # 4. Path for annotated images (YOLO saves them here)
    # Note: Check if YOLO creates a 'predict' subfolder inside 'internship_seg'
    annotated_folder = os.path.join("runs", "segment", "internship_seg")
    
    # 5. Stitch Video with FFmpeg (Starting at 0001 per your latest frames)
    print("--- Stitching Segmented Video ---")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-framerate", "30",
        "-i", f"{annotated_folder}/frame_%04d.png", 
        "-i", AUDIO_FILE,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",
        OUTPUT_VIDEO
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"\nSUCCESS! Segmented video saved as {OUTPUT_VIDEO}")
        print("Performance metrics are available in: runs/segment/internship_seg/")
    except subprocess.CalledProcessError:
        print("\nERROR: FFmpeg failed. Check if the output images are .jpg or .png.")

if __name__ == "__main__":
    main()