# driver.py
from src.vision.screen_capture import run_capture
from src.vision.computer_vision import run_detection
import threading
import os
import time  # Needed to sleep in the main loop

def threads():
        # Create output directory if it doesn't exist
    output_path = "src/vision/raw_frames"
    os.makedirs(output_path, exist_ok=True)
    
    # Create and start threads as daemon threads
    capture_thread = threading.Thread(
        target=run_capture,
        kwargs={"output_path": output_path},
        daemon=True  # Mark thread as daemon
    )
    detection_thread = threading.Thread(
        target=run_detection,
        daemon=True  # Mark thread as daemon
    )
    
    capture_thread.start()
    detection_thread.start()
    
    # Keep the main thread alive to listen for Ctrl+C
    try:
        while True:
            time.sleep(1)  # Just waiting for an interrupt
    except KeyboardInterrupt:
        print("KeyboardInterrupt caught. Exiting...")


def main():
    threads()
    
if __name__ == "__main__":
    main()
