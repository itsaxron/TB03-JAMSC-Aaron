import api, coh, overheads, profit_loss

def main():
    forex = api.getExchangeRate()
    maxOverhead = overheads.getMaxOverhead(forex)
    losses = profit_loss.getProfitLosses(forex)
    cohLosses = coh.getcohLosses(forex)

    with open('summary_report.txt', 'w') as f:
        f.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n')
        f.write(f'[HIGHEST OVERHEAD] {maxOverhead[0].upper()}: SGD{maxOverhead[1]}\n')

        if cohLosses == []: # this means there were no losses
            f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(cohLosses)):
                f.write(f'[CASH DEFICIT] DAY: {cohLosses[i][0]}, AMOUNT: {cohLosses[i][1]}\n')

        if losses == []: # this means there were no losses
            f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(losses)):
                f.write(f'[PROFIT DEFICIT] DAY: {losses[i][0]}, AMOUNT: {losses[i][1]}\n')

    print("Created summary_report.txt")

main()