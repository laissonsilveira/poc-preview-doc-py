#!/usr/bin/env python3
import sys
from preview_generator.manager import PreviewManager

file_in = sys.argv[1]
file_out = sys.argv[3]

manager = PreviewManager(file_out, create_folder= True)
path_to_preview_image = manager.get_jpeg_preview(file_in, width=140)

print(path_to_preview_image)