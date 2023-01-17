import os 
import csv

budget_data_csv = "../Resources/budget_data.csv"

output_text = "output.txt"

total_months = 0
net_total_profit = 0

revenue_change = 0 
previous_profit = 0
average_change = 0

max_increase = 0
max_decrease = 0
max_month = 0
min_month = 0

total_profit_list = []
revenue_change_list = []
date_list = []



with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1 # used += as a shortcut for total_months = total_months + 1 ; gives us the total months
    #print(total_months) to check work
        date_list.append(row[0])


        net_total_profit = net_total_profit + (int(row[1])) # gives us the net total profit
        total_profit_list.append(int(row[1])) # adds the total profit to the list. 
        # I had originally tried using total_profit_list.append(net_total_profit), but this was not giving me the list that I needed. I couldn't figure out why
    #print(total_profit_list) to check work

    for i in range(len(total_profit_list)-1): # tell the code to loop through each item in the profit/losses list (row 1)
        revenue_change_list.append(total_profit_list[i+1] - total_profit_list[i]) # find the difference: previous profit - current profit 
    #print revenue_change_list to check work 
        average_change = round(sum(revenue_change_list)/len(revenue_change_list),2) #find average change using the revenue_change_list and round to 2 decimal points
    #print(average_change) to check work
        
        max_increase = max(revenue_change_list) #use python maximum function to find the max value in revenue_change_list
    #print(max_increase) to check
        max_decrease = min(revenue_change_list) #use python min function 
    #print(max_decrease) to check 

        max_month = revenue_change_list.index(max(revenue_change_list)) + 1 #https://www.geeksforgeeks.org/python-list-index/
        min_month = revenue_change_list.index(min(revenue_change_list)) + 1

        max_increase_date = date_list[max_month]
        max_decrease_date = date_list[min_month] 
    # print(max_increase_index) #gives us index 81, which is Aug 16th 
    # print(max_decrease_index) #gives us index 51, which is Feb 14th 
    # +1 because we want the next month, which is the month associated with the greatest change; the first time through the loop, there is no change



# printing and csv writing function learned with tutor Alysia Won
with open(output_text, "w") as csvfile: 
  budget_analysis_final = (
    f"Financial Analysis \n" 
    f"---------------- \n"
    f"Total Months: {total_months} \n" 
    f"Total Profit: ${net_total_profit} \n"
    f"Average Change: ${average_change} \n"
    f"Greatest Increase in Profits: {max_increase_date} ${max_increase} \n"
    f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease} \n" )
  print(budget_analysis_final)

  csvfile.write(budget_analysis_final)