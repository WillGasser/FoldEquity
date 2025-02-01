from mss import mss
from mss.tools import to_png
import numpy as np
import time
import os

output_path = "raw_frames/"

if not os.path.exists(output_path):
    raise Exception(f"Output directory specified as: {output_path} does not exist.")
    
frame = 0
    
while True:
    with mss() as sct:
        output_file = os.path.join(output_path, f"frame-{frame}.png")
        sct.shot(output=output_file, mon=1)
    frame += 1
    time.sleep(1)
    