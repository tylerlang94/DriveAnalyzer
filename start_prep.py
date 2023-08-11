import os.path

directory = "C:\Apps\MTS\DriveAnalysis"
csv_path = "C:\Apps\MTS\DriveAnalysis\DriveAnalysis.csv"
log_path = "C:\Apps\MTS\DriveAnalysis\DriveAnalysisLog.txt"
check_file = os.path.isfile(csv_path)
check_log = os.path.isfile(log_path)                      
check_dir = os.path.exists(directory)

def checkDir():
    if check_dir == False:
        os.mkdir(directory)

def checkCSV():
    if check_file == False:
        open(csv_path, "w")

def checkLog():
    if check_log == False:
        open(log_path, "w")

def prep():
    checkDir()
    checkCSV()
    checkLog()


