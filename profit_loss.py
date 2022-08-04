import csv
from pathlib import Path

def profitloss_function(forex):
    path = str(Path.cwd())
    path += '\csv_reports\Profits and Loss.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)

    losses = []

    for i in range(len(rows)):
        if i == 0:
            continue
        if rows[i][4] < rows[i-1][4]:
            losses_amount = []
            losses_amount.append("{:.2f}".format(float(rows[i][0])))
            losses_amount.append("{:.2f}".format(forex*(int(rows[i-1][4]) - int(rows[i][4]))))

            losses.append(losses_amount)

    return losses