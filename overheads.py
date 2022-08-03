
import csv
from pathlib import Path

def overhead_function(forex):

    path = str(Path.cwd())
    path += '\csv_reports\Overheads.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)

    max = 0
    maxHeader = [] #list that returns [max overhead, which overhead]

    for i in range(len(rows)):
        if max < float(rows[i][1]):
            max = float(rows[i][1])
            maxHeader = [rows[i][0], "{:.2f}".format(max * forex)]

    return maxHeader
