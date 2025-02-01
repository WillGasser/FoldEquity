# driver.py
from src.vision.screen_capture import run_capture
from src.vision.computer_vision import run_detection
import threading
import os

def main():
    # Create output directory if it doesn't exist
    output_path = os.path.join("vision", "raw_frames")
    os.makedirs(output_path, exist_ok=True)
    
    # Create and start threads
    capture_thread = threading.Thread(
        target=run_capture,
        kwargs={"output_path": output_path}
    )
    detection_thread = threading.Thread(target=run_detection)
    
    capture_thread.start()
    detection_thread.start()
    
    # Wait for both threads to complete (which they won't in this case)
    capture_thread.join()
    detection_thread.join()

if __name__ == "__main__":
    main()