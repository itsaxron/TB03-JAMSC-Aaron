# import csv module library
# import Path module library from pathlib
import csv
from pathlib import Path

# create define function overhead_function() with parameter 'forex'
def overhead_function(forex):

# function Path.cwd() gets the current working directory for user's device
# str(Path.cwd()) converts the current working directory into a string
# the stringed current working directory is then assigned to 'path' variable
# += extends the current working directory by '\csv_reports\Overheads.csv', and it assigns it to as the new directory for 'path' variable
    path = str(Path.cwd())
    path += '\csv_reports\Overheads.csv'

# variable 'rows' is assigned to an empty list
# it will be easier to append into once data is extracted from the .csv file
    rows = []

# with statement is used for open() function, also doubles down exception handling situation
# open() function is used to open the specific .csv file in 'read' mode, and is classified as 'f'
    with open(path, 'r') as f:
    # csv.reader(parameter = f) used to read the .csv file
    # the read .csv file is assigned to variable 'csvreader'
        csvreader = csv.reader(f)
    # next() is used in csv reading to skip the first row in the .csv file, which is the header for the data values
        next(csvreader)

    # using for loop, the parameter row is created for the data extracted into csvreader
    # using .append(parameter = row), the data extracted will be added into the variable 'row' which is an empty list
    # the previously empty list assigned to 'row' will now be a nested list of the contents in the .csv file
        for row in csvreader:
            rows.append(row)

# assigned variable 'max' to the value of 0
# this will make it easier for the for loop code to add and compare values when running through the nested list
    max = 0

# create a new variable 'maxDetails' that is assigned to an empty list
# once appended and ran through the for loop code, it will return [Max Overhead Category, Overhead Value]
    maxDetails = [] 

# for loop, variable i in the range the number of lists in the nested list assigned to 'rows'
# to find the specific range, len() function is used and it will count the number of lists in the nested list assigned to 'rows'
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
        # rows[i][0] where i will be assigned to the list with the highest value and [0] will take the first value of the list corresponding to [i], which is the name of the overhead category
        # "{:.2f}".format(value) is used to format and round off the value to two decimal places
        # max * forex, where max equals to the highest found value, will multiply with the currency conversion rate from 'forex'
            maxDetails = [rows[i][0], "{:.2f}".format(max * forex)]

    # returns maxDetails, which includes a single list of the highest value and the overhead category correposnding to it
    # it will return in this format: [Overhead category corresponding to the highest value, Highest Value overhead amount]
    return maxDetails