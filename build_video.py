#!/usr/bin/env python3

import os
from lib.organize import *
from lib.timestamps import *
from lib.process import *

current_dir_path = os.getcwd()
topic_transitions_dir_path = current_dir_path + '/recording/topic-transitions'

standardize_transition_segment_lengths(topic_transitions_dir_path)
rename_topic_transition_segments_to_be_in_tens(topic_transitions_dir_path)

calculate_timestamps_and_write_to_excel_and_yt_desc(current_dir_path)

combine_video_files(current_dir_path)
add_chapters_to_video_file(current_dir_path)
