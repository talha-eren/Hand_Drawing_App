# Hand Drawing Application (Mediapipe + OpenCV)

This project uses **Mediapipe** and **OpenCV** to track hand movements from a webcam and allows drawing on the screen using the index fingertip.  
The drawing process is also recorded and saved as an **`.avi` video file**.

---

## Project Files
- `hand_tracking.py` → Main Python script for hand tracking and drawing  
- `requirements.txt` → Required Python libraries  
- `hand_drawing.avi` → Example output video generated after running the program  

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/talha-eren/hand-drawing-app.git 
   cd hand-drawing-app
Install dependencies:

bash
pip install -r requirements.txt
Usage
Run the script:

bash
python hand_tracking.py
The webcam window will open.

Move your index fingertip to draw on the screen.

All drawings will be saved automatically in hand_drawing.avi.

Press ESC to exit the program safely.

Technologies
Python

OpenCV

Mediapipe

NumPy

Notes
Output video is recorded in .avi format. If you face playback issues, try VLC Media Player.

The project currently supports single-hand tracking only.
