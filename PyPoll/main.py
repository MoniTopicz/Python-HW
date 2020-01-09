import csv
import os

#path to the csv file
election_data= os.path.join('Resources','election_data.csv')

#set variables
candidate_names = []
candidate_votes = []
vote_summary = {}
      
#read the csv file
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    #read the header rows and burnout the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #loop through the data
    for row in csvreader:
        candidate_votes.append(row[0])
        candidate_names.append(row[2])
    
    #list of candidates and total votes for each candidate
    vote_summary = {}
    for i in range(len(candidate_names)):
        candidate = candidate_names[i]
        if not vote_summary.get(candidate):
            vote_summary[candidate] = 1
        else:
            vote_summary[candidate] += 1


print(f"Election Results:")
print(f"-------------------------")
print(f"Total Votes: {len(candidate_votes)}")
print(f"-------------------------")
sum_votes = len(candidate_votes)
max_votes = 0
max_candidate_name = ""
for key,value in vote_summary.items():
    print(key + ': ' + str(round(value*100/sum_votes,3)) + '%' + ' ' + str((value)))
    if value > max_votes:
        max_candidate_name = key
        max_votes = value
print(f"-------------------------")
print(f"Winner: {str(max_candidate_name)}")