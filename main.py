import api, coh, overheads, profit_loss

def main():
    forex = api.api_function()
    overheads_max = overheads.overhead_function(forex)
    pnl_losses = profit_loss.profitloss_function(forex)
    coh_losses = coh.coh_function(forex)

    with open('summary_report.txt', 'w') as f:
        f.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n')
        f.write(f'[HIGHEST OVERHEAD] {overheads_max[0].upper()}: SGD{overheads_max[1]}\n')

        if coh_losses == []: # this means there were no losses
            f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(coh_losses)):
                f.write(f'[CASH DEFICIT] DAY: {coh_losses[i][0]}, AMOUNT: SGD{coh_losses[i][1]}\n') 

        if pnl_losses == []: # this means there were no losses
            f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(pnl_losses)):
                f.write(f'[PROFIT DEFICIT] DAY: {pnl_losses[i][0]}, AMOUNT: SGD{pnl_losses[i][1]}\n')

    print("Output Successful")

main()