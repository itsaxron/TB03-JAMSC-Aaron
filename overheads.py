import csv
from pathlib import Path

# create define function overhead_function() with parameter 'forex'
def overhead_function(forex):
    path = str(Path.cwd())
    path += '\csv_reports\Overheads.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)

# assigned variable 'max' to the value of 0
# this will make it easier for the for loop code to add and compare values when running through the nested list
    max = 0

# create a new variable 'maxDetails' that is assigned to an empty list
# once appended and ran through the for loop code, it will return [Max Overhead Category, Overhead Value]
    maxDetails = [] #list that retuns [max overhead, which overhead]

    for i in range(len(rows)):

# if function used within the for loop
# initially, max = 0 and variable i = 0
# float(rows[i][1] will look through the nested list in 'rows'
# it will start and look at the first list (as i = 0 at first), and [1] will look at the second value in the list checked
# if the value found will be checked it it is bigger than the current value of 'max'
# at the start of the code, max = 0. Thus, the value found from the first list will be used as a benchmark and compared when running through the range of lists in 'rows' nested list
# if there is a value found in any of the list that is greater than the current value in 'max', max = float(rows[i][1]) will assign it as the new value for 'max'
        if max < float(rows[i][1]):
            max = float(rows[i][1])

# once the for loop runs through the entire range of lists in the nested lists 'rows', it will end with the highest overhead value after comparing through the lists
            maxDetails = [rows[i][0], "{:.2f}".format(max * forex)]

    return maxDetails

