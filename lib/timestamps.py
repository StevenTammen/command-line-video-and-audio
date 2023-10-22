'''
These functions mostly relate with the automation that:

- Calculates timestamps based off of segment durations
- Pairs these timestamps with the matching labels

They are basically functions to do the icky math
involved in determining timestamps, so that they do
not have to be figured out manually.
'''

import math

def get_video_segment_names():
    # Read expected video segment names from spreadsheet read into an array
   
    segment_names = ['### Section one', '#### Subsection 1.1', '#### Subsection 1.2', '### Section 2', '#### Subsection 2.1']
    return segment_names

def get_duration_map_based_off_of_processed_recordings():
    # cd into recording/processed directory
   
    # for each mp4 file in directory, store the file name and full duration (not just like 05:20, but a seconds/milliseconds or whatever value)
    # in an ordered array of tuples. Should be in order of file names ascending
   
    duration_map = [('10_processed_with_savvycut', 125.5),
    ('20_processed_with_savvycut', 600.5),
    ('30_processed_with_savvycut', 240.5),
    ('40_processed_with_savvycut', 60.5),
    ('50_processed_with_savvycut', 180.5)
    ]
    return duration_map
   
def get_string_value_of_time(numerical_time):
   
    # This function assumes the var numerical_time is in seconds (rather than milliseconds or whatever).
    # Otherwise, before anything else, run whatever you have to in order to convert numerical_time to seconds.
    # numerical_time = numerical_time * 1000
   
    # There are 60 seconds in an hour, and 60 minutes in an hour. That's where 3600.00 comes from
    # We use a decimal version of this number to ensure all math is done with floats
    hours = math.floor(numerical_time/3600.0)
   
    # https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
    minutes = math.floor((numerical_time % 3600.0)/60.0)
   
    seconds = math.floor(numerical_time % 60)
   
    if(hours > 0):
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"

def get_timestamps(duration_map, topic_transition_duration = 0):
   
    # Stores the calculated timestamps as formatted strings. Should be the same length as the array of headers
    timestamps = []
   
    # Keeps track of where in the video you are after each segment has been completed
    cumulative_duration = 0
   
    # The first segment starts at 0:00
    timestamps.append('0:00')
   
    # We only go through N - 1 segments. Since the first timestamo is always 0:00, this loop
    # is only responsible for N - 1 timestamps, not N timestamps. All the timestamps but the first.
    for recording in duration_map[:-1]:
        duration = recording[1]
        last_section_ended_at = cumulative_duration + duration
        string_timestamp = get_string_value_of_time(last_section_ended_at)
        timestamps.append(string_timestamp)
        cumulative_duration += (duration + topic_transition_duration)
       
    return timestamps

def get_labeled_timestamps(segment_names, timestamps):
    if(len(timestamps) != len(segment_names)):
        raise Exception("The number of recordings must match the number of video segments tracked in Excel")
    else:
       
   
    # Do replacement of ### and #### to properly do indentation based on nesting