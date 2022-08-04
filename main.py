# imports the files api.py, coh.py, overheads.py and profit_loss.py
import api, coh, overheads, profit_loss

# create a define function main()
def main():

    # assign functions for each of the module to be executed in this main.py file
    forex = api.api_function()
    overheads_max = overheads.overhead_function(forex)
    losses = profit_loss.profitloss_function(forex)
    cohdeficit = coh.coh_function(forex)

# with statement is used for open() function, also doubles down exception handling situation
# open() function is used to create the summary_report.txt file in 'write' mode, with encoding of 'UTF-8' and is classified as 'f'
    with open('summary_report.txt', 'w', enconding = "UTF-8") as f:
    
    # to_symbol = 'SGD' is the currency used to display the values in the summary report
        to_symbol = 'SGD'

    # .write() function used to write a line in the .txt file
    # using f-strings, use the variable 'to_symbol' and 'forex' so the string can be interchangeable if values were to be changed
    # \n includes to python to return a new line in the .txt file
        f.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = {to_symbol}{forex}\n')
    # overheads_max[0] takes the first value in the list, which is the overhead category name
    # .upper() function will full capitalized the overhead category
    # overheads_max[1] takes the second value in the list, which is the corresponding highest value among the overheads
        f.write(f'[HIGHEST OVERHEAD] {overheads_max[0].upper()}: {to_symbol}{overheads_max[1]}\n')

    # if else function
    # if coh returns an empty list, means there is no deficits found, and thus will print the surplus message
        if coh == []:
            f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')

    # else, for i variable in the range of the number of lists (deficits) found in cohdeficit, it will write the deficit statement accordingly
    # if there is multiple deficits found, the \n will create a new line and add the multiple deficit statements
        else:
            for i in range(len(cohdeficit)):
                f.write(f'[CASH DEFICIT] DAY: {cohdeficit[i][0]}, AMOUNT: {to_symbol}{cohdeficit[i][1]}\n')

    # if else function, similar to coh
    # if losses returns an empty list, means there is no deficits found, and thus will print the surplus message
        if losses == []: # this means there were no losses
            f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
    # else, for i variable in the range of the number of lists (deficits) found in losses, it will write the deficit statement accordingly
    # if there is multiple deficits found, the \n will create a new line and add the multiple deficit statements
        else:
            for i in range(len(losses)):
                f.write(f'[PROFIT DEFICIT] DAY: {losses[i][0]}, AMOUNT: {to_symbol}{losses[i][1]}\n')

    # will print a message 'Created: Summary_Report.txt' in the terminal if .txt file output is successful   
    print('Created: Summary_Report.txt')

# will run the main() define function
main()