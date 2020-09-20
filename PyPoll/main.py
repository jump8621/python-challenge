import os
import csv


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
   
    Total_votes = len(voter_ID)    
    # print(Total_votes)
    # print(numb_votes)    
    # print(can_list)
    
    saved_x=0

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(Total_votes))
    print("----------------------------")


    for x in can_list:
        
        print(x + ": (" + str(numb_votes[x]) + ")  " + "{:.3f}".format(numb_votes[x]/(len(voter_ID))*100))
       

        if (numb_votes[x] > saved_x):
            saved_x = numb_votes[x]
            saved_name = x    

    print("----------------------------")
    print("Winner: " + saved_name)    
    print("----------------------------")
        
    #f=open("analysis.txt", "w+")   

    file = 'analysis/analysis.txt'

with open(file, 'w') as text:

   #text.write ("Election Results\n--------------------------")
   text.writelines("Election Results\n")
   text.writelines("----------------------------\n")
   text.writelines("Total Votes: " + str(Total_votes) + "\n")
   text.writelines("----------------------------\n")
   for x in can_list:
        
    text.writelines(x + ": (" + str(numb_votes[x]) + ")  " + "{:.3f}".format(numb_votes[x]/(len(voter_ID))*100) +"%\n")
   text.writelines("----------------------------\n")
   text.writelines("Winner: "+ saved_name + "\n")
   text.writelines("----------------------------\n")


text.close