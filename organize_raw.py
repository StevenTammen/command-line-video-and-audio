#!/usr/bin/env python3

from lib.organize import *

current_dir_path = os.getcwd()
raw_dir_path = current_dir_path +'/raw'
rename_raw_segments_to_be_in_tens(raw_dir_path)
