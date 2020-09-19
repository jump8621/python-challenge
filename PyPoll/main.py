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
    can_list = []

    numb_votes = {}

    for row in csvreader:
        
        voter_ID.append(row[0])
       
        electees = row[2]
        if electees not in can_list:
            can_list.append(electees)

        if electees not in numb_votes:
            numb_votes[electees] = 1
        else:
            numb_votes[electees] = numb_votes[electees] + 1
   
        
    print(len(voter_ID))
    print(numb_votes)    
    print(can_list)
    for x in can_list:
        
        print(x,numb_votes[x],(numb_votes[x]/(len(voter_ID))*100))
        print(x,< value numb_votes[x])
        
        #if numb_votes[x] > saved x then winner!
    #print(winner)