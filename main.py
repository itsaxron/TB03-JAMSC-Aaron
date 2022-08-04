import api, coh, overheads, profit_loss

def main():
    forex = api.api_function()
    overheads_max = overheads.overhead_function(forex)
    losses = profit_loss.profitloss_function(forex)
    cohdeficit = coh.coh_function(forex)

    with open('summary_report.txt', 'w') as f:
        to_symbol = 'SGD'
        f.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = {to_symbol}{forex}\n')
        f.write(f'[HIGHEST OVERHEAD] {overheads_max[0].upper()}: {to_symbol}{overheads_max[1]}\n')

        if coh == []:
            f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(cohdeficit)):
                f.write(f'[CASH DEFICIT] DAY: {cohdeficit[i][0]}, AMOUNT: {to_symbol}{cohdeficit[i][1]}\n')

        if losses == []: # this means there were no losses
            f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(losses)):
                f.write(f'[PROFIT DEFICIT] DAY: {losses[i][0]}, AMOUNT: {to_symbol}{losses[i][1]}\n')
                
    print('Created: Summary_Report.txt')

main()