import wmi
import datetime


from csv_class import CSVWriter

# Get the current date and time
now = datetime.datetime.now()

directory = "C:\Apps\MTS\DriveAnalysis"
csv_path = "C:\Apps\MTS\DriveAnalysis\DriveAnalysis.csv"
log_path = "C:\Apps\MTS\DriveAnalysis\DriveAnalysisLog.txt"
fieldnames = ('Date', 
              'DriveLetter', 
              'FreeSpace', 
              'TotalSpace', 
              'PercentFree')

# Create the filename for the CSV file

def driveInfo():
    c = wmi.WMI ()
    for d in c.Win32_LogicalDisk():
        driveLetter = d.Caption
        freeSpace = float(d.FreeSpace)/1000000000
        totalSpace = float(d.Size)/1000000000
        percentFree = (freeSpace/totalSpace * 100)
        print( driveLetter, freeSpace, totalSpace, percentFree, d.DriveType)

    csv_write = CSVWriter(filename=csv_path, fieldnames=fieldnames)

    drive_info = {'Date': now,
            'DriveLetter': driveLetter, 
            'FreeSpace': freeSpace, 
            'TotalSpace': totalSpace, 
            'PercentFree': percentFree
            }


    csv_write.write_row(drive_info)



    csv_write.close()

