import os
import csv 

csvpath = os.path.join('..', 'Py_Resources', 'budget_data.csv')


total_months = []
Start_number = 0 #counter
net_total_Losses = []
average_Profits = []
#average_Losses = []
total_Profit_Losses = []
rev_average_Change = []
prevRevenue = 0
month_of_change = []
greatest_Increase = ["", 0]
greatest_Decrease = ["", 999999999999999999]



with open(csvpath, newline= "") as csvfile:

	csvreader = csv.reader(csvfile, delimiter= ",")
	#lines = csvfile.read()
	#print(lines)
	for row in csvreader:
		#print(row)
		for row in csvreader:
			total_months.append(row[0])
			total_Profit_Losses.append(row[1])


			Number_months = len(total_months)
			Start_number = Start_number + int(row[1])

			revenuechange = int(row[1]) - prevRevenue
			prevRevenue = int(row[1])

			rev_average_Change.append(revenuechange)
			month_of_change.append(row[0])

			if revenuechange > greatest_Increase[1]:
				greatest_Increase[0] = row[0]
				greatest_Increase[1] = revenuechange
			if revenuechange < greatest_Decrease[1]:
				greatest_Decrease[0] = row[0]
				greatest_Decrease[1] = revenuechange

Average_Revenue = sum(rev_average_Change) / len(rev_average_Change)


print("Financial_Analysis") #,"/n")
print("--------------------")
print(f'Total Months: {Number_months}')
print(f'Total: $ {Start_number}')
print(f'Greatest Increase in Profits:  {greatest_Increase[0]} + (${greatest_Increase[1]})')
print(f'Greatest Decrease in Profits:  {greatest_Decrease[0]} + (${greatest_Decrease[1]})')


output_path = os.path.join("..", "PyBank", "PyBank.txt")

file = open(output_path, 'w')

file.write("Financial_Analysis") #,"/n")
file.write("\n")
file.write(f'Total Months: {Number_months}')
file.write("\n")
file.write(f'Total: $ {Start_number}')
file.write("\n")
file.write(f'Greatest Increase in Profits:  {greatest_Increase[0]} + (${greatest_Increase[1]})')
file.write("\n")
file.write(f'Greatest Decrease in Profits:  {greatest_Decrease[0]} + (${greatest_Decrease[1]})')

file.close()












	