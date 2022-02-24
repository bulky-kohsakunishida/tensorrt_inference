#!/usr/bin/env python3

import ScaledYOLOv4
import sys
import glob
import re

if len(sys.argv) < 3:
	print("Please design config file and folder name!")
	sys.exit

config_file = sys.argv[1]
image_name = sys.argv[2]

inf = ScaledYOLOv4.ScaledYOLOv4(config_file)
inf.LoadEngine()

inf.InferenceImage(image_name)

