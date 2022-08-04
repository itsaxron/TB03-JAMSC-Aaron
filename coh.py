import csv
from pathlib import Path

def coh_function(forex):
    path = str(Path.cwd())
    path += '\csv_reports\Cash on Hand.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)

    deficit = []

    for i in range(len(rows)):
        if i == 0:
            continue
        if rows[i][1] < rows[i-1][1]:
            deficit_amount = []
            deficit_amount.append("{:.2f}".format(float(rows[i][0])))
            deficit_amount.append("{:.2f}".format(forex*(int(rows[i-1][1]) - int(rows[i][1]))))

            deficit.append(deficit_amount)

    return deficit