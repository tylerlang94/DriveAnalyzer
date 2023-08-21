import pandas as pd

directory = "C:\Apps\MTS\DriveAnalysis"
csv_path = "C:\Apps\MTS\DriveAnalysis\DriveAnalysis.csv"

data = pd.read_csv(csv_path, parse_dates='DateTime', 'FreeSpace')
