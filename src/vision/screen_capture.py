# screen_capture.py
"""
This module captures screenshots of a target poker window.
It uses MSS to grab the window's image, pygetwindow to select the window,
and saves the screenshots to a specified output folder.
"""

import os
import time
from mss import mss
from mss.tools import to_png
import pygetwindow as gw

def choose_window():
    """
    Presents a list of windows whose titles contain poker-related keywords and
    prompts the user to choose one.

    Returns:
        str: The title of the selected window, or None if no valid window is selected.
    """
    # Define poker-related keywords.
    poker_keywords = [
        "lobby", "poker", "texas", "holdem", "hold'em", "casino", "cards",
        "no limit", "play", "tournament", "heads-up", "ring", "cash game",
        "freeroll", "table", "seat", "turn", "chips", "bet", "dealer", "blinds"
    ]
    
    # Get all non-empty window titles.
    all_titles = [title for title in gw.getAllTitles() if title.strip()]
    
    # Filter titles that contain any of the poker-related keywords (case-insensitive).
    filtered_titles = []
    for title in all_titles:
        for kw in poker_keywords:
            if kw.lower() in title.lower():
                filtered_titles.append(title)
                break  # Stop checking keywords once a match is found.
    
    if not filtered_titles:
        print("No poker-related windows found.")
        return None

    print("Available poker-related windows:")
    for idx, title in enumerate(filtered_titles, 1):
        print(f"{idx}. {title}")
    
    choice = input("Enter the number of the window to capture: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(filtered_titles):
            return filtered_titles[index]
        else:
            print("Choice out of range.")
            return None
    except Exception as e:
        print("Invalid input:", e)
        return None

def get_window_bbox(title):
    """
    Returns the bounding box of the window with the specified title
    in a format that mss.grab() accepts.

    Args:
        title (str): The title of the window.

    Returns:
        dict: A dictionary with 'top', 'left', 'width', 'height' or None if not found.
    """
    windows = gw.getWindowsWithTitle(title)
    if windows:
        win = windows[0]
        return {
            "top": win.top,
            "left": win.left,
            "width": win.width,
            "height": win.height
        }
    else:
        return None

def run_capture(output_path="raw_frames/"):
    """
    Runs the capture loop: selects a window, then continuously captures
    screenshots of the active window and saves them to the specified directory.

    Args:
        output_path (str): The directory where screenshots will be stored.
    """
    # Let the user choose the target window.
    window_title = choose_window()
    if window_title is None:
        raise Exception("No valid poker window selected.")
    print(f"Selected window: {window_title}")

    # Verify the output directory exists.
    if not os.path.exists(output_path):
        raise Exception(f"Output directory specified as: {output_path} does not exist.")

    frame = 0
    while True:
        # Only take a screenshot if the chosen window is the active one.
        active_window = gw.getActiveWindow()
        if active_window is None or active_window.title != window_title:
            print(f"Window '{window_title}' is not active. Skipping screenshot.")
            time.sleep(1)
            continue

        bbox = get_window_bbox(window_title)
        if bbox is None:
            print(f"Window with title '{window_title}' not found.")
            time.sleep(1)
            continue

        with mss() as sct:
            screenshot = sct.grab(bbox)

        timestamp = int(time.time() * 1000)
        output_file = os.path.join(output_path, f"frame_{timestamp}.png")
        to_png(screenshot.rgb, screenshot.size, output=output_file)
        print(f"Saved {output_file}")

        frame += 1
        time.sleep(0.1)

if __name__ == "__main__":
    run_capture()