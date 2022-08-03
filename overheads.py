import csv
from pathlib import Path

def getMaxOverhead(forex):
    path = str(Path.cwd())
    path += '\csv_reports\Overheads.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)

    max = 0
    maxDetails = [] #list that retuns [max overhead, which overhead]

    for i in range(len(rows)):
        if max < float(rows[i][1]):
            max = float(rows[i][1])
            maxDetails = [rows[i][0], "{:.2f}".format(max * forex)]

    return maxDetails

