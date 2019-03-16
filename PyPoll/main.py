	
import os
import csv

csvpath = os.path.join('..', 'Py_Resources', 'election_data.csv')

voter_List=[]
candidate_List=[]
county_List=[]
votes_TotalCast = 0
candidate_TotalCast = [0,0,0,0]
win_Percent = []
election_Winner = 0
election_Name =""


with open (csvpath, newline= "") as handler:
    pollData = csv.reader(handler)
    #lines = handler.read()
    #print(lines)
	
	for row in pollData:
	print(type(row))
		continue
    
#def Election_Results(election_dataset):

#total number of votes cast

#complete list of candidates who recieved votes

#percent of votes each candidate won

#total number of votes candidate won

#winner of election based on popular vote

print("Election Results") #,"/n")
print("--------------------")
print(f'Total Votes: {votes_TotalCast}')
print("--------------------")
print(f'{candidate_List[0]}: ({win_Percent} + {candidate_TotalCast})')#in range(4)^^^^
print("--------------------")
print(f'Winner: {election_Winner}')