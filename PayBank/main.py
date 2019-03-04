import os
import csv
csvpath= os.path.join('..','Resources',"budget_data.csv")
Net_Profits=0
total_months=0
average_change=0
prev_profits=0
greatest_increase=["",0]
greatest_decrease=["",99999999999999999999999999]
profit_changes=[]

with open(csvpath,newline='')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
    rows=[]
    count=0
    change_add=0

    for row in csvreader:
    
        total_months +=1
        Net_Profits +=int(row[1])
        profit_change=int(row[1])-prev_profits
        #print(profit_change)
        prev_profits=int(row[1])
        #print(prev_profits)
        if( profit_change> greatest_increase[1]):
            greatest_increase[1]=profit_change
            greatest_increase[0]=row[0]
        if(profit_change< greatest_decrease[1]):
            greatest_decrease[1]=profit_change
            greatest_decrease[0]=row[0]
        change_add+=profit_change
        count+=1
        average= change_add/count


print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(Net_Profits))
print("Average Change: " + "$" + str(average))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")  