# vision/computer_vision.py
"""
This module processes captured screenshots to detect game state.
It uses OpenCV for image processing and updates the Game model.
"""

import os
import time
import cv2
from src.game_logic.game_objects import Game, Player  # Assuming game_objects.py is in root

# Configuration
INPUT_DIR = os.path.join("vision", "raw_frames")
PROCESSING_DELAY = 1  # Seconds between processing attempts

def detect_game_state(frame_path):
    """Placeholder for actual CV logic"""
    # In real implementation, use OpenCV to process image and extract:
    # - Player positions
    # - Chip counts
    # - Cards
    # - Bets
    # - Game phase
    
    print(f"Processing frame: {frame_path}")
    return Game(players=[
        Player(name="Player 1", chip_amount=1500),
        Player(name="Player 2", chip_amount=1500)
    ])

def run_detection():
    """Main detection loop"""
    processed_files = set()
    
    while True:
        # Get list of available frames
        try:
            files = sorted([
                f for f in os.listdir(INPUT_DIR)
                if f.startswith("frame_") and f.endswith(".png")
            ], key=lambda x: os.path.getmtime(os.path.join(INPUT_DIR, x)))
        except FileNotFoundError:
            continue
            
        # Process only new files
        new_files = [f for f in files if f not in processed_files]
        
        for file in new_files:
            frame_path = os.path.join(INPUT_DIR, file)
            game_state = detect_game_state(frame_path)
            # Here you would integrate the game state with your application
            processed_files.add(file)
            
        time.sleep(PROCESSING_DELAY)