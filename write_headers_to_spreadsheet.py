#!/usr/bin/env python3

import os
from lib.write_to_files import *

current_dir_path = os.getcwd()
write_content_headers_to_segments_spreadsheet(current_dir_path)
