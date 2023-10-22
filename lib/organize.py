'''
These functions mostly relate with the automation that:

- Controls which video segments are present in the directories
- Controls what they are called

They are basically meta functions to organize all the files
and the get them ready for processing and concatenation.
'''

import os
import subprocess
import shlex

# TODO
def automatically_organize_gopro_recordings():
    '''
    Automatically concatenates the videos that span across multiple 
    recording chunks (which is most of them, in practice).

    Then calls rename_raw_segments_to_be_in_tens()
    '''
    return

def rename_raw_segments_to_be_in_tens(raw_dir_path):
    '''
    Preserves order, but renames everything to multiples of 10.
    So like 10.mp4, 20.mp4, and so on.

    Many recording programs will spit out videos that are in the right
    order (that is, in terms of how things were recorded), but with 
    kind of gross file names full of dates and times. And the format
    is not consistent across programs either.

    Standardizing the names like this (and using multiples of 10) makes it
    easy to add new segments wherever you want them in the order. You can
    then call this function again to re-baseline the order (make everything
    only multiples of 10 again). Although be sure that the processed/ and
    topic-transitions/ files are then also updated in the same way.

    At present, this function presupposes that the recordinsg are
    .mp4 files.
    '''
    segment_names = [f for f in os.listdir(raw_dir_path) if f.endswith('.mp4')]
    segment_names.sort()

    counter = 10
    for segment_name in segment_names:
        new_name = raw_dir_path + '/' + str(counter) + '.mp4'
        os.rename(raw_dir_path + '/' + segment_name, new_name)
        counter += 10

def rename_topic_transition_segments_to_be_in_tens(topic_transitions_dir_path):
    '''
    TODO - better description
    '''
    transition_segment_names = [f for f in os.listdir(topic_transitions_dir_path) if f.endswith('.mp4')]
    transition_segment_names.sort()

    counter = 10
    for segment_name in transition_segment_names:
        new_name = topic_transitions_dir_path + '/' + str(counter) +'-' + str(counter + 10) + '.mp4'
        os.rename(topic_transitions_dir_path + '/' + segment_name, new_name)
        counter += 10

# TODO
def rename_processed_segments_to_be_in_tens():
    # Will only really use if after adding new segment = have to re-call rename_raw_segments_to_be_in_tens()
    # Want order to match between raw and processed. Hence why this would then need to be called
    return


# I will change this function later to actually autogenerate the transition segments eventually. Maybe?
# Right now I manually record the segments, and then use ffmpeg to standardize them to 2.0 seconds
def generate_topic_transition_segments(topic_transitions_dir_path, duration = 2.0):
    # Eventually:
    # Pulls from list of segments on the 'Full' tab of the segments spreadsheet
    # Only pulls non-dud segments
    # Can change duration based upon input float

    transition_segment_names = [f for f in os.listdir(topic_transitions_dir_path) if f.endswith('.mp4')]
    for segment_name in transition_segment_names:
        file_name_parts = os.path.splitext(segment_name)
        base_name = file_name_parts[0]
        extension = file_name_parts[1]

        # Standardize length to {duration} using ffmpeg.
        # Starts just after first second of video, and goes for {duration} time
        # On running command in shell: https://stackoverflow.com/a/72741384
        input_file = topic_transitions_dir_path + '/' + segment_name
        output_file = topic_transitions_dir_path + '/' + base_name + '-shortened' + extension
        subprocess.run(shlex.split(f'ffmpeg -i {input_file} -ss 00:01 -t {duration} {output_file}'))

        # Overwrite initial file. Cannot overwrite directly within ffmpeg command. See this StackOverflow:
        # https://stackoverflow.com/questions/28877049/issue-with-overwriting-file-while-using-ffmpeg-for-converting
        os.remove(input_file)
        os.rename(output_file, input_file)

# TODO
def remove_dud_segments():
    # Deletes the dud video files
    # Removes the dud rows from the 'Full' tab of the segments spreadsheet
    return