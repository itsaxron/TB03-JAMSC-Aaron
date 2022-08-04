import api, coh, overheads, profit_loss

def main():
    forex = api.api_function()
    overheads = overheads.overhead_function(forex)
    losses = profit_loss.profitloss_function(forex)
    coh = coh.coh_function(forex)

    with open('summary_report.txt', 'w') as f:
        f.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n')
        f.write(f'[HIGHEST OVERHEAD] {overheads[0].upper()}: SGD{overheads[1]}\n')

        if coh == []: # this means there were no losses
            f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(coh)):
                f.write(f'[CASH DEFICIT] DAY: {coh[i][0]}, AMOUNT: {coh[i][1]}\n')

        if losses == []: # this means there were no losses
            f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(losses)):
                f.write(f'[PROFIT DEFICIT] DAY: {losses[i][0]}, AMOUNT: {losses[i][1]}\n')
                
    print('Created: Summary_Report.txt')

main()