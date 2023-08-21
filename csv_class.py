import csv
import os


class CSVWriter:
    def __init__(self, filename, fieldnames):
        self.filename = filename
        self.fieldnames = fieldnames
        self.file_exists = os.path.exists(self.filename)
        
        if not self.file_exists:
            self.file = open(self.filename, 'w', newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
            self.writer.writeheader()
        else:
            self.file = open(self.filename, 'a', newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)

    def write_row(self, data):
        ordered_data = {key: data[key] for key in self.fieldnames}
        self.writer.writerow(ordered_data)

    def close(self):
        self.file.close()
