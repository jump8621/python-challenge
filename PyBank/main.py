import os
import csv

def average(numbers):

    return sum(numbers) / len(numbers)

#csvpath = os.path.join('Resources','budget_data.csv')
budget_data_csv = os.path.join('Resources','budget_data.csv')


# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    month_total =[]
    pl_value =[]
    total =0
    savedvalue = 0

    # Loop through the data
    for row in csvreader:
        value = int(row[1])
        total = value + total
        if (savedvalue != 0):
            profitloss = value - savedvalue            
            pl_value.append(profitloss)
        savedvalue = value
        month_total.append(row[0])

    #print(len(month_total))
    #print(total)
    profit_average = average (pl_value)
    #print (profit_average)
    maxprofit = max (pl_value)
    #print(f'maxprofit ${maxprofit}')
    maxindex = pl_value.index(maxprofit)
    #print(month_total[maxindex+1])
    minprofit = min(pl_value)
    #print(f'minprofit ${minprofit}')
    minindex = pl_value.index(minprofit)
    #print(month_total[minindex+1])
     

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(month_total)))
    print("Total: $" + str(total))
    print("Average Change: $" + "{:.3f}".format(profit_average))
    print("Greatest Increase in Profits: " + month_total[maxindex+1] + "  $" + str(maxprofit))
    print("Greatest Decrease in Profits: " + month_total[minindex+1] + " $" + str(minprofit))


file = 'analysis/analysis.txt'

with open(file, 'w') as text:

   text.writelines("Financial Analysis\n")
   text.writelines("----------------------------\n")
   text.writelines("Total Months: " + str(len(month_total)) + "\n")
   text.writelines("Total: $" + str(total) + "\n")
   text.writelines("Average Change: $" + "{:.3f}".format(profit_average) + "\n")
   text.writelines("Greatest Increase in Profits: " + month_total[maxindex+1] + "  $" + str(maxprofit) +  " \n")
   text.writelines("Greatest Decrease in Profits: " + month_total[minindex+1] + " $" + str(minprofit))

text.close
