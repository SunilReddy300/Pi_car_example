from picarx import Picarx
import time
import subprocess




subprocess.run(["python3", "rasp_color_detect.py"])
subprocess.run(["python3", "Lane_extract.py"])
