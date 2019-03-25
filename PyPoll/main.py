	
import os
import csv

csvpath = os.path.join('..'/'PyPoll'/'election_data.csv')


candidate_List=[]
county_List=[]
Total_VotesCast = 0
candidate_TotalCast = [0,0,0,0]
win_Percent = []
winner_election = 0
election_Name = ""


with open (csvpath, newline= "") as handler:
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

for row in candidateTotalCast:
	win_Percent.append(round(row/Total_VotesCast,4))
	#print(winPercent)

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
#print(f'{candidate_List[0]}: ({win_Percent} + {candidate_TotalCast})')#in range(4)^^^^
#print("--------------------")
#print(f'Winner: {winner_election}')






#output_path = os.path.join("..", "PyBank", "PyBank.txt")

#file = open(output_path, 'w')

#file.write("Financial_Analysis") #,"/n")
#file.write("\n")
#file.write(f'Total Months: {Number_months}')
#file.write("\n")
#file.write(f'Total: $ {Start_number}')
#file.write("\n")
#file.write(f'Greatest Increase in Profits:  {greatest_Increase[0]} + (${greatest_Increase[1]})')
#file.write("\n")
#file.write(f'Greatest Decrease in Profits:  {greatest_Decrease[0]} + (${greatest_Decrease[1]})')

#file.close()

















