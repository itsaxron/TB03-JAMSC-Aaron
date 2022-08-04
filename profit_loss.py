# import csv module library
# import Path module library from pathlib
import csv
from pathlib import Path

# create a define function profitloss_function() with 'forex' as parameter
def profitloss_function(forex):

# function Path.cwd() gets the current working directory for user's device
# str(Path.cwd()) converts the current working directory into a string
# the stringed current working directory is then assigned to 'path' variable
# += extends the current working directory by '\csv_reports\Profits and Loss.csv', and it assigns it to as the new directory for 'path' variable
    path = str(Path.cwd())
    path += '\csv_reports\Profits and Loss.csv'

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

# variable 'losses' is assigned to an empty list
# it will be easier to append into
    losses = []

# for loop, variable i in the range the number of lists in the nested list assigned to 'rows'
# to find the specific range, len() function is used and it will count the number of lists in the nested list assigned to 'rows'
    for i in range(len(rows)):

    # based on the assignment brief, need to calculate the differences in net profit between each day
    # as the first day does not have any days previous to compare to, will be best to skip the day
    # the first day is the first list in the nested list assigned to 'row', which is the value [0] in python
    # if i ==0, then continue is used to skip the number 0, and start the for loop from number 1 (which will start from the second list in the nested list)
        if i == 0:
            continue
    # the for loop will start from the second list in the nested list, thus i == 1 at first
    # if rows[i][4] < rows[i-1][4] creates a loop to go through all the lists in the nested list range
    # where [i] is the current day of the list checked, and [i-1] is the previous day of the current day checked
    # the [4] after [i] and [i-1] checks the fifth value in the list, which will be the net profit value
    # once the net profit value is found, it will compare the net profit value from the previous day (i-1) to the current day (i)
    # if previous day net profit value is bigger than the current day net profit value, it will be counted as a deficit as there is a decrease 
        if rows[i][4] < rows[i-1][4]:

        # variable 'losses_amount' is assigned to an empty list
        # this code will run if there is a deficit/decrease in the net profit value found when comparing inbetween days
        # line 69 finds the day (current day) that corresponds to where the deficit/decrease was found
        # in line 69, rows[i][0] where i equals to the list of the current day the deficit was found, and [0] will take the first value in the list which is the Day, to get the day number corresponding to the deficit
        # line 70 finds and calculates the differences between the current day and the previous day the deficit/decrease was found
        # line 70 int(rows[i-1][4]) - int(rows[i][4]) where [i-1][4] takes the net profit of the previous day, and [i][4] takes the net profit of the current day, minusing both
        # once the difference between the net profit of current and previous day is found, it is multiplied by the conversion rate using forex*
        # int() function is used to be able to mathemtically equate both numbers
        # .append() is used to add into the empty list assigned to 'losses_amount'
        # "{:.2f}".format(value) is used to format and round off the value to two decimal places

            losses_amount = []
            losses_amount.append("{:.2f}".format(float(rows[i][0])))
            losses_amount.append("{:.2f}".format(forex*(int(rows[i-1][4]) - int(rows[i][4]))))

        # once the loop calculates and differences and finds the Day number corresponding to the deficit, it will go through the whole nested list till it reaches the max range
        # the newly furnished list will be assigned into 'losses_amount'
        # once the i variable goes through the whole range, using .append() function, it will add in the new lists from 'losses_amount' and assign it to 'losses' variable
            losses.append(losses_amount)

    # returns losses, which includes the nested list of the days which has deficit net profit values
    # it will return in this format: [Day of the deficit, Value of the deficit net profit amount]
    return losses