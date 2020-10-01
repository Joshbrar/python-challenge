import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
toal_profitloss = 0
print (csvpath)
date_list = []
profit_loss_list = []

with open(csvpath) as my_csv_file:
    #print(my_csv_file)
    read_my_csv_file  = csv.reader(my_csv_file, delimiter=",")
    header = next(read_my_csv_file)
    print(header)
  #  date_list =[ row[0] for row[0] in read_my_csv_file]
  #  print(date_list[0])

    for row in read_my_csv_file:
      date_list.append(str(row[0]))
      profit_loss_list.append( int(row[1]))
      toal_profitloss = toal_profitloss + int(row[1])

#print(date_list,"\n")
#print(profit_loss_list,"\n")

no_months = len(date_list)


# find revenue change
revenue_change = []

for x in range(1, len(profit_loss_list)):
  revenue_change.append((int(profit_loss_list[x]) - int(profit_loss_list[x-1])))

# print (revenue_change)
revenue_average = sum(revenue_change)/len(revenue_change)


greatest_increase = max(revenue_change)
greatest_increase_dt = str(date_list[revenue_change.index(max(revenue_change))+1])

greatest_decrease = min(revenue_change)
greatest_decrease_dt = str(date_list[revenue_change.index(min(revenue_change))+ 1])



#print output to Screeean Results
print("Financial Analysis")

print("....................................................................................")
print("Total Months:  " + str(no_months))
print("Total Profit:  " + str(toal_profitloss))
print ("Revenue Average " + str(revenue_average))
print("Greatest Increase in Profits:   " + str(greatest_increase_dt) + "  ("  +  str(greatest_increase) + ")")
print("Greatest Decrease in Profits:   " + str(greatest_decrease_dt) + "  ("  +  str(greatest_decrease) + ")")


# write to a file

output_file = os.path.join( "..", "Resources", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(no_months) + "\n")

    file.write("Total Profit: " + "$" +  str(toal_profitloss) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + greatest_increase_dt + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + greatest_decrease_dt + " " + "$" + str(greatest_decrease) + "\n")

    file.close()
