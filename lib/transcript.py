'''
These functions mostly relate with the automation that:

- Grabs the transcript information off of the YouTube video
- Builds shortcodes with the timing information to support page-internal links
'''


from .general_utility import *

# https://github.com/jdepoix/youtube-transcript-api
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id, num_subsegments_to_combine_for_each_transcript_line):
    transcript_lines = []
    transcript_as_list_of_dicts = YouTubeTranscriptApi.get_transcript(video_id)
    for chunk in chunks(transcript_as_list_of_dicts, num_subsegments_to_combine_for_each_transcript_line):
        if(chunk != None):
            timestamp = get_string_value_of_time(chunk[0]['start'])
            # https://stackoverflow.com/questions/7271482/getting-a-list-of-values-from-a-list-of-dicts
            just_text_values = [d['text'] for d in chunk]
            text = ' '.join(just_text_values)
            hugo_timestamp = build_hugo_timestamp(video_id, timestamp, text)
            transcript_lines.append(hugo_timestamp)

    return '\n'.join(transcript_lines)
