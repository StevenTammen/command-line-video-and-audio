'''
These functions are just general utility functions.
Reading in files, that sort of thing.
'''

import os
from pathlib import Path
import pandas as pd
import openpyxl
from .config import config

def read_in_file(file_path):
    with open(file_path, "r", encoding="utf8") as f:
      return f.read()

def read_in_full_df(spreadsheet_path):
    spreadsheet_file = Path(spreadsheet_path)
    if(not spreadsheet_file.exists()):
        raise Exception("Segments.xlsx file does not exist. Are you running this script in the right directory?")
    df = pd.read_excel(spreadsheet_path, "Full", index_col=0)
    return df

def get_headers_list(spreadsheet_path):
  df = read_in_full_df(spreadsheet_path)
  headers_list = df['Header'].tolist()
  return headers_list

def get_internal_timestamps_list(spreadsheet_path):
  df = read_in_full_df(spreadsheet_path)
  internal_timestamps_list = df['Internal timestamp'].tolist()
  return internal_timestamps_list

def get_non_internal_headers_list(spreadsheet_path):
    df = read_in_full_df(spreadsheet_path)
    headers_list = df['Header'].tolist()
    internal_timestamps_list = df['Internal timestamp'].tolist()
    non_internal_headers_list = []
    for i in range(len(headers_list)):
        if(str(internal_timestamps_list[i]).lower() == "nan"):
            non_internal_headers_list.append(headers_list[i])
    return non_internal_headers_list

# https://stackoverflow.com/a/40347279
def fast_scandir(dirname):
    # Ignores recording subdirectories, since we only care about the possibility of discussion pages
    # when recursing. (Don't name any discussion page 'recording'. Just don't)
    subfolders= [f.path for f in os.scandir(dirname) if (f.is_dir() and f.name != 'recording')]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

def set_spreadsheet_column_widths(spreadsheet_path):
    wb = openpyxl.load_workbook(spreadsheet_path)
    full_sheet = wb['Full']
    initial_sheet = wb['Initial']
    for spreadsheet_column in  config.spreadsheet_columns:
        #  First, for 'Full' sheet
        full_sheet.column_dimensions[spreadsheet_column.col].width = spreadsheet_column.width
        # Then, for 'Initial' sheet
        initial_sheet.column_dimensions[spreadsheet_column.col].width = spreadsheet_column.width
    wb.save(spreadsheet_path)

def safe_open_w(path):
  '''
  Open "path" for writing, creating any parent directories as needed.

  https://stackoverflow.com/a/23794010
  '''
  os.makedirs(os.path.dirname(path), exist_ok=True)
  return open(path, 'w', encoding="utf8")