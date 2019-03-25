	
import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')


candidate_List=[]
county_List=[]
Total_VotesCast = 0
candidate_TotalCast = [0,0,0,0]
win_Percent = []
winner_election = 0
election_Name = ""

with open (csvpath, newline = "") as handler:
	pollData = csv.reader(handler)
	for row in pollData:
		for row in pollData:
			Total_VotesCast = Total_VotesCast + 1
			candidate_List.append(row[2])
			candidate_List = list(set(candidate_List))

with open (csvpath, newline = "") as handler:
	pollData = csv.reader(handler)
	for row in pollData:
		for row in pollData:
			picked = row[2]
			picked = candidate_List.index(picked) 
			candidate_TotalCast[picked] += 1

for row in candidate_TotalCast:
	win_Percent.append(round(row/Total_VotesCast))
	#print(win_Percent)

print("Election Results") #,"/n")
print("--------------------")
print(f'Total Votes: {Total_VotesCast}')
print("--------------------")

for x in range(len(candidate_TotalCast)):
	print(str(candidate_List[x])+": "+str(win_Percent[x])+" ("+str(candidate_TotalCast[x])+")")
	if winner_election < candidate_TotalCast[x]:
		winner_election = candidate_TotalCast[x]
winner_election = candidate_TotalCast.index(winner_election)

	

finalResult = zip(candidate_List,win_Percent,candidate_TotalCast)
finalResult = list(finalResult)



#print("Election Results") #,"/n")
#print("--------------------")
#print(f'Total Votes: {Total_VotesCast}')
#print("--------------------")
#print(str(candidate_List[x])+": "+str(win_Percent[x])+" ("+str(candidate_TotalCast[x])+")")
#print("--------------------")
#print(f'{finalResult}')
print("--------------------")
print("Winner: "+ candidate_List[winner_election])



output_path = os.path.join("..", "PyPoll", "PyPoll.txt")

file = open(output_path, 'w')

file.write("Election Results") #,"/n")
file.write("\n")
file.write(f'Total Votes: {Total_VotesCast}')
file.write("\n")
file.write(f'{finalResult}')
#file.write(str(candidate_List[x])+": "+str(win_Percent[x])+" ("+str(candidate_TotalCast[x])+")")
file.write("\n")
file.write("Winner: "+ candidate_List[winner_election])

file.close()

















