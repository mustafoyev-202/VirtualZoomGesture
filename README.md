# Hand Tracking Image Drag and Drop 🖐️🖼️

## Features

- Real-time hand tracking
- Interactive image manipulation
- Two-hand pinch-to-zoom
- Single-hand drag functionality

## Prerequisites

- Python 3.7+
- OpenCV
- cvzone
- Sample image file

## Installation

```bash
pip install opencv-python cvzone
```

## Usage

1. Replace `"sample.jpg"` with your desired image path
2. Run the script: `python main.py`

### Interactions

- **Two-finger pinch**: Zoom image
- **Closed fist**: Drag image
- **Press 'q'**: Quit application

## Requirements

- Webcam
- Good lighting
- Clear hand visibility

## Notes

- Ensure a clear background for best hand detection
- Adjust detection confidence in `HandDetector()` if needed