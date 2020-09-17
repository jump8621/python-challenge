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
    month_list =[]
    total =0
    savedvalue = 0

    # Loop through the data
    for row in csvreader:
        value = int(row[1])
        total = value + total
        if (savedvalue != 0):
            profitloss = value - savedvalue            
            month_list.append(profitloss)
        savedvalue = value
        month_total.append(row[0])

    print(len(month_total))
    print(total)
    profit_average = average (month_list)
    print (profit_average)
    maxprofit = max (month_list)
    print(f'maxprofit ${maxprofit}')
    maxindex = month_list.index(maxprofit)
    print(month_total[maxindex+1])
    minprofit = min(month_list)
    print(f'minprofit ${minprofit}')
    minindex = month_list.index(minprofit)
    print(month_total[minindex+1])
    
    print(len(month_list))
    print(month_list)
    print(month_total)


WriteTxtFile = open ("analysis.txt", "w")
file = 'analysis/output.txt'

with open(analysis.txt, 'w') as text:

   writelines()

    

