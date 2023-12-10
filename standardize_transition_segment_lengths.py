#!/usr/bin/env python3

from lib.organize import *

current_dir_path = os.getcwd()
topic_transitions_dir_path = current_dir_path +'/recording/topic-transitions'
standardize_transition_segment_lengths(topic_transitions_dir_path)
