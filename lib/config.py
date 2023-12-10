class Config:
    def __init__(self, spreadsheet_columns):
        self.spreadsheet_columns = spreadsheet_columns

class SpreadsheetColumn:
    def __init__(self, name, col, width):
        self.name = name
        self.col = col
        self.width = width

spreadsheet_columns = []
spreadsheet_columns.append(SpreadsheetColumn('File', 'B', 25))
spreadsheet_columns.append(SpreadsheetColumn('Header', 'C', 60))
spreadsheet_columns.append(SpreadsheetColumn('Internal timestamp', 'D', 17))
spreadsheet_columns.append(SpreadsheetColumn('Timestamp', 'E', 15))

config = Config(spreadsheet_columns)
