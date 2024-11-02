#!/usr/bin/env python3

import re
import os
import subprocess
import shlex

current_dir_path = os.getcwd()
segment_names = [f for f in os.listdir(current_dir_path) if f.endswith('.mp4')]

# https://www.geeksforgeeks.org/python-sort-given-list-of-strings-by-part-the-numeric-part-of-string/
segment_names.sort(key=lambda segment_name : list(
    map(int, re.findall(r'\d+', segment_name)))[0]) 

for segment_name in segment_names:
    input_file = current_dir_path + '/' + segment_name
    output_file = current_dir_path + '/' + segment_name.replace('.mp4', '_libx265.mp4')
    # https://unix.stackexchange.com/questions/28803/how-can-i-reduce-a-videos-size-with-ffmpeg
    subprocess.run(shlex.split(f'ffmpeg -i {input_file} -vcodec libx265 -crf 20 {output_file}'))
