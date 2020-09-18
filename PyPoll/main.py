import os
import csv

def average(numbers):
    return sum(numbers) / len(numbers)

def sum(numbers):
    total=0
    total = total + 1
    return total

election_data_csv = os.path.join('resources', 'election_data.csv')

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    voter_ID = []




    for row in csvreader:
        #voter_ID = int(row[0])
        
        #voter_ID = row [0]
        #total_voters = voter_ID.append(int(row[0]))
        
        voter_ID.append(row[0])
        #sum(total_voters)

        

        

      #  value = int(row[1])
       # total = value + total
        #if (savedvalue != 0):
         #   profitloss = value - savedvalue            
          #  pl_value.append(profitloss)
        #savedvalue = value
        #month_total.append(row[0])

    print(len(voter_ID))

