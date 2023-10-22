'''
These functions are just general utility functions.
Reading in files, that sort of thing.
'''

def read_in_file(file_path):
  with open(file_path, "r", encoding="utf8") as f:
    return f.read()