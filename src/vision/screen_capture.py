from mss import mss
from mss.tools import to_png
import pygetwindow as gw
import time
import os

def choose_window():
    # Define poker-related keywords
    poker_keywords = [
    "lobby",
    "poker",
    "texas",
    "holdem",
    "hold'em",
    "casino",
    "cards",
    "no limit",
    "play",
    "tournament",
    "heads-up",
    "ring",
    "cash game",
    "freeroll",
    "table",
    "seat",
    "turn",
    "chips",
    "bet",
    "dealer",
    "blinds"
]
    
    # Get all non-empty window titles
    all_titles = [title for title in gw.getAllTitles() if title.strip()]
    
    # Filter titles that contain any of the poker-related keywords (case-insensitive)
    filtered_titles = []
    for title in all_titles:
        for kw in poker_keywords:
            if kw.lower() in title.lower():
                filtered_titles.append(title)
                break  # stop checking keywords once a match is found
    
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

# Let the user choose the target window
window_title = choose_window()
if window_title is None:
    raise Exception("No valid poker window selected.")

print(f"Selected window: {window_title}")

# Directory where screenshots will be stored.
# Ensure that this folder exists.
output_path = "raw_frames/"
if not os.path.exists(output_path):
    raise Exception(f"Output directory specified as: {output_path} does not exist.")

def get_window_bbox(title):
    """
    Returns the bounding box of the window with the specified title
    in a format that mss.grab() accepts.
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

    output_file = os.path.join(output_path, f"frame-{frame}.png")
    to_png(screenshot.rgb, screenshot.size, output=output_file)
    print(f"Saved {output_file}")

    frame += 1
    time.sleep(1)
