import os
import csv

#define variables
rows = 0
profit_t = 0
dif_t = 0
max_dif = 0
date_max_dif = ""
prior_profit = 0
min_dif = 0
date_min_dif = ""
dif = 0
total_dif = 0

path_in = os.path.join(".","Resources", "budget_data.csv")
with open(path_in) as infile:
    reader = csv.reader(infile)

    header = next(reader)
    print(header)
    for row in reader:
        print(row)
   #file = open('Resources\budget_data.csv', 'r')
    #next(file)



# code to skip first header line

        rows = rows + 1
        if rows > 1:
            prior_profit = profit
    #      
        #row = row.strip()
        #row = row.split(",")
        year_date = row[0]
        profit = row[1]
        profit = int(profit)

        if rows > 1:
            dif = profit - prior_profit
            total_dif = total_dif + dif 
            
        if dif > max_dif:
            max_dif = dif
            date_max_dif = year_date

        if dif < min_dif:
            min_dif = dif
            date_min_dif = year_date

            profit_t = profit_t + profit
    # print(year_date, profit)
    infile.close()
print("Financial Analysis")
print("------------------------------")
  
print("Total Months", rows)

print("Total", profit_t)
average_dif = total_dif/(rows - 1)

print("Average Change", average_dif)
print("Greatest Increase in Profits", max_dif)
print(date_max_dif)
print("Greatest Decrease in Profits", min_dif)
print(date_min_dif)
