import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")

#identify lists and starting amounts
Number_Month = []
Profit_loss = []
Net_change = []
Previous_PL = 0
lineNumber = 0
changeTime = 0
GreatestInc = 0
GreatestIncDate = 0
GreatestDec = 0
GreatestDecDate = 0


#opena and read csv (commna)
with open(csvpath,'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header in csv file
    header = next(csvreader)
    #loop through data
    for row in csvreader:
        lineNumber += 1
        Number_Month.append(row[0])
        Profit_loss.append(int(row[1]))
        #calculate netchange and find greatest increase and decrease change
        if lineNumber != 1:
            currentNetChange = int(row[1]) - Previous_PL
            Net_change.append(currentNetChange)
            changeTime = changeTime + 1
            if currentNetChange > GreatestInc:
                GreatestInc = currentNetChange
                GreatestIncDate = row[0] 
            if currentNetChange < GreatestDec:
                GreatestDec = currentNetChange
                GreatestDecDate = row[0]

        Previous_PL = int(row[1])

#print the results 
print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Number_Month)}")
print(f"Total: ${sum(Profit_loss)}")
print(f"Average Change: ${(sum(Net_change)/changeTime):3f}")
print(f"Greatest Increase in Profits: {GreatestIncDate} $({GreatestInc})")
print(f"Greatest Decrease in Profits: {GreatestDecDate} $({GreatestDec})")


# create a open output file
output_file = os.path.join("budget_final.csv")
with open(output_file, "w") as file:
    writer = csv.writer(file)

    # Write the header row
    file.write(f"Financial Analysis")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(Number_Month)}")
    file.write("\n")
    file.write(f"Total: ${sum(Profit_loss)}")
    file.write("\n")
    file.write(f"Average Change: ${(sum(Net_change)/changeTime):3f}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {GreatestIncDate} $({GreatestInc})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {GreatestDecDate} $({GreatestDec})")
    file.write("\n")

