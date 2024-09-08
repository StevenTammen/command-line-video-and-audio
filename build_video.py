#!/usr/bin/env python3

import os
import sys
from lib.organize import *
from lib.timestamps import *
from lib.process import *

from lib.transcript import *

# Note:
# This script is step 4/6 in the normal processing workflow:
# 1) Run scaffold_recordings.py in the content dir.
# 2) Actually make the recordings (and put in raw/ subdirectory). Update segments.xlsx if necessary (internal timestamp headers).
# 3) Run remove_silence.py in the recording dir. Update segments.xlsx if necessary (internal timestamp times). Update content file if necessary (subject tags, passage tags, video only sections).
# 4) Run build_video.py in the recording dir. Validate it looks right (via VLC), and upload to YouTube. (Copy-paste the title and automatically-built description)
# 5) Wait a day or whatever to let YouTube auto-generate the transcript. Then add the video URL to content page frontmatter, and run write_back_to_content_file.py in the recording dir.
# 6) Run hugo-preprocessor, check over diff, push to website, make video public.

# Note:
# This script assumes silence has already been removed from content recording segments. (See remove_silence.py)
# It also assumes that segments.xlsx already exists, and that:
#   1) segments.xlsx has the correct headers in the correct order, and
#   2) segments.xlsx has internal timestamps defined for any segment-internal timestamps

current_dir_path = os.getcwd()
clvaa_path = os.path.dirname(sys.argv[0])

# Build topic transition segments
generate_topic_transition_slides(current_dir_path, clvaa_path)
build_topic_transition_segments(current_dir_path)

# Calculate timestamps based on post-silence-removal content recording segment boundaries
calculate_timestamps_and_write_to_excel_and_yt_desc(current_dir_path)

# Combine all the segments into a single video file
combine_video_files(current_dir_path)

# Add chapter metadata to the single video file
add_chapters_to_video_file(current_dir_path)
