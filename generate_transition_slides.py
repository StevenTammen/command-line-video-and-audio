#!/usr/bin/env python3

from lib.organize import *
import sys
import os

current_dir_path = os.getcwd()
clvaa_path = os.path.dirname(sys.argv[0])

generate_topic_transition_slides(current_dir_path, clvaa_path)
