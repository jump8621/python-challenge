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

    print(len(month_total))
    print(total)
    profit_average = average (pl_value)
    print (profit_average)
    maxprofit = max (pl_value)
    print(f'maxprofit ${maxprofit}')
    maxindex = pl_value.index(maxprofit)
    print(month_total[maxindex+1])
    minprofit = min(pl_value)
    print(f'minprofit ${minprofit}')
    minindex = pl_value.index(minprofit)
    print(month_total[minindex+1])
     

file = 'analysis/analysis.txt'

with open(file, 'w') as text:

   text.write ("Financial Analysis\n----------------------------\nTotal Months: 86\nTotal: $38382578\nAverage Change: $-2315.12\nGreatest Increase in Profits: Feb-2012 ($1926159)\nGreatest Decrease in Profits: Sep-2013 ($-2196167)")

text.close
