import csv

def reader_csv_file(file):
    text = file.file.read().decode()
    reader = csv.DictReader(text.splitlines())
    rows = [row for row in reader]
    return rows
