import os
import csv

def average(numbers):
    return sum(numbers) / len(numbers)

def sum(numbers):
    total=0
    total = total + 1
    return total

#funtion to get unique values
#def unique(all_canidates):

election_data_csv = os.path.join('resources', 'election_data.csv')

with open(election_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    voter_ID = []
    can_list = []

    numb_votes = {}
    #numb_votes = dict()
    

    #numb_votes['candidate'] = 'Khan'
    #numb_votes["candidate"] = can_list
    #numb_votes["votes"] = 1 

    for row in csvreader:
        
        
        voter_ID.append(row[0])
       
        electees = row[2]
        if electees not in can_list:
            can_list.append(electees)
        if electees not in numb_votes:
            numb_votes[electees] = 1
        else:
            numb_votes[electees] = numb_votes[electees] + 1
        #numb_votes[electees] = 1
        #numb_votes[electees] = can_list + 1
        #numb_votes = {electees}
        #if "candidate" == 'Khan':
            #numb_votes: "votes" + 1
        #elif "candidate" == 'Correy':
            #numb_votes: "votes" + 1
        #elif "candidate" ==  'Li':
            #numb_votes: "votes" + 1
        #elif "candidate" == "O'Tooley":
            #numb_votes: "votes" + 1 

        


   
        
    print(numb_votes)    
    print(len(voter_ID))
    print(can_list)
    for x in can_list:

        print(x,numb_votes[x],(numb_votes[x]/(len(voter_ID))*100))
        
    #print(f'{numb_votes["candidates"]}{numb_votes["votes"]}') 
    #print("candidates" + "votes")

   # print(all_canidates)
        #all_canidates = unique(electees)
       # for word in unique_all_canidates:
        #    if word not in unique_all_canidates:
         #       unique_all_canidates.append(word)
        #for word in unique_all_canidates:
         #   print(word)
        

        

      #  value = int(row[1])
       # total = value + total
        #if (savedvalue != 0):
         #   profitloss = value - savedvalue            
          #  pl_value.append(profitloss)
        #savedvalue = value
        #month_total.append(row[0])


