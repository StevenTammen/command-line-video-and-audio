'''
These functions mostly relate with the automation that:

- Updates _index.md and segments.xlsx with the results
  of application execution
- Builds a text file containing the text that will go
  in the YouTube description

They are basically functions that write back calculated
timestamps and the like to the content file and Excel
spreadsheet that tracks recording segments, and also
write to new files as necessary.
'''

from pathlib import Path
from .general_utility import *
import pandas as pd
import re

content_section_re_pattern = re.compile(r'^{{% content %}}((?:.|\n)+?){{% /content %}}', re.MULTILINE)
content_header_re_pattern = re.compile(r'^[#]+ [^{\n]+', re.MULTILINE)
def get_content_headers(recording_dir_path):
    '''
    Gets the content headers from the content page corresponding to
    the recording as a list of strings.
    '''

    # First convert path to the content version. Here, we are implicitly
    # assuming that the folder structure for the content project is
    # exactly mirrored in the recordings folder
    content_dir_path = recording_dir_path.replace("/mnt/c/Dropbox/recordings/", "/mnt/c/R/")

    # TODO: support index.md as well as _index.md, for discussion pages
    # Get text of just the content section on the page
    content_page_path = content_dir_path + '/' + '_index.md'
    full_page_contents = read_in_file(content_page_path)
    content_section_on_page = content_section_re_pattern.search(full_page_contents)
    if(content_section_on_page != None):
        # First content section on page will be the one for the page itself,
        # rather than being a content section for a nested discussion page
        content_section_on_page = content_section_on_page.group(1)
    else:
        raise Exception("Content page does not have a properly formed content section. Please check and make sure page is complete.")

    # Get content headers. Findall() returns a list of strings that match the regular expression.
    # It is a list of tuples that gets returned instead, if you use capture group(s).
    content_headers = content_header_re_pattern.findall(content_section_on_page)
    if(content_headers == None):
        raise Exception("Content section does not have any headers. Please check and make sure page is complete.")

    # Trim any trailing spaces
    content_headers = list(map(str.strip, content_headers))
    
    # We don't care about the first header, since it will always be '## Content'
    return (content_headers[1:])

def write_to_existing_segments_spreadsheet(spreadsheet_path, content_headers):
    '''
    Overwrites 'Initial' sheet in segments.xlsx spreadsheet, updating
    it with current state of content headers
    '''
    # Have to use openpyxl here since mode='a' and therefore if_sheet_exists='replace'
    # only work with openpyxl, for whatever reason
    with pd.ExcelWriter(spreadsheet_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        data = {'File': '', 'Header': content_headers, 'Internal timestamp':'', 'Timestamp':''}
        df = pd.DataFrame(data)
        df.to_excel(writer, sheet_name='Initial')
    set_spreadsheet_column_widths(spreadsheet_path)

def write_to_new_segments_spreadsheet(spreadsheet_path, content_headers):
    '''
    Creates segments.xlsx spreadsheet, with two sheets called 'Full' and 'Initial'.
    They start out the same, but 'Full' will be updated over time, whereas 'Initial'
    always just matches the current state of content headers.
    '''
    with pd.ExcelWriter(spreadsheet_path, engine='openpyxl') as writer:
        data = {'File': '', 'Header': content_headers, 'Internal timestamp':'', 'Timestamp':''}
        df = pd.DataFrame(data)
        df.to_excel(writer, sheet_name='Full')
        df.to_excel(writer, sheet_name='Initial')
    set_spreadsheet_column_widths(spreadsheet_path)

def write_content_headers_to_segments_spreadsheet(recording_dir_path):
    '''
    TODO: description
    '''
    content_headers = get_content_headers(recording_dir_path)

    spreadsheet_path = recording_dir_path + '/' + 'segments.xlsx'
    spreadsheet_file = Path(spreadsheet_path)
    if(spreadsheet_file.exists()):
        write_to_existing_segments_spreadsheet(spreadsheet_path, content_headers)
    else:
        write_to_new_segments_spreadsheet(spreadsheet_path, content_headers)

# TODO
def write_file_names_and_timestamps_back_to_spreadsheet():
    return

# TODO
def write_embedded_video_and_timestamps_back_to_content_file():
    # Adds timestamps to section under summary. Adds embedded video link to video shortcode.
    # Adds timestamps under each header metadata shortcode that starts a segment

    # Triggers re-run of static site preprocessor so that changes roll up to aggregation pages

    # Does *not* automatically commit and push in git
    return

# TODO
def write_youtube_description_to_text_file():
    # Will overwrite this file if it already exists
    return