import os
import csv
from collections import OrderedDict
from operator import itemgetter

csvpath= os.path.join('..','Resources',"election_data.csv")
votes=0
winner_votes =0
total_candidates=0
more_voted=["",0]
candidate_options=[]
candidate_votes={}


with open(csvpath,newline='')as csvfile:
    csvreader=csv.DictReader(csvfile)
    print(csvreader)
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        votes+=1
        total_candidates=row["Candidate"]
        #print (total_candidates)
        if row["Candidate"] not in candidate_options:
            candidate_options.append (row["Candidate"])
            candidate_votes[row["Candidate"]]=1
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    print("Election Results")
    print("----------------------------------------")
    print("Total Votes " + str(votes))
    print("-----------------------------------------")
    

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)
print("---------------------------------------------")
print("Winner: " + str(winner[0]))
print("----------------------------------------------")
