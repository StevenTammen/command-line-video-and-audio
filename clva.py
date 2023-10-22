'''
This script assumes you are located in the root folder for
a given piece of content, as described in [link].

It also assumes you have already recorded all your segments,
based on the list contained in segments.xlsx. 

(For now: also assume topic-transitions have been recorded).
'''

from lib.organize import *
from lib.process import *
from lib.timestamps import *
from lib.upload import *

# Rename raw recording files to be be in form of
# 10.mp4, 20.mp4, etc.

# Process video files

# Generate timestamps



headers = get_headers()
duration_map = get_duration_map_based_off_of_processed_recordings()
print(get_timestamps(duration_map))