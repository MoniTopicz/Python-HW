import csv
import os

#path to the csv file
budget_data= os.path.join('Resources','budget_data.csv')


#set variables
total_months = []
profit_list = []
prev_profit_loss = 0
greatest_increase = 0
greatest_decrease = 999999999999
profit_total = []
ttl_profit_total = 0

#read the csv file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read the header rows and burnout the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #reading through rows after header and count months and set profit list row
    for row in csvreader:
        profit_list.append(row[1])
        total_months.append(row[0])
       
       
        # calculating total
        profit_total = int(row[1]) 
        
        if(profit_total):
            ttl_profit_total = ttl_profit_total + profit_total
    

    
    #calculating average change
    diff_list = [int(profit_list[i+1]) - int(profit_list[i]) for i in range(len(profit_list) - 1)]
    
    #greatest increase and greatest decrease in profits
    for i in range(len(profit_list)):
        profit_loss = profit_list[i]
        
        net_income = int(profit_loss) - int(prev_profit_loss)
        if net_income >= 0:
            if net_income > greatest_increase:
                greatest_increase = net_income
                greatest_increase_num = i
        else:
            if net_income < greatest_decrease:
                greatest_decrease = net_income
                greatest_decrease_num = i
        prev_profit_loss = profit_loss
    
    
                
print(f"Financial Analysis")
print(f"-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${(ttl_profit_total)}")
print(f"Average Change: ${(sum(diff_list)/len(diff_list))}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_num]} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_num]} ${greatest_decrease}")

