import os
import csv

#path for file
csvPath = os.path.join('Resources','budget_data.csv')

avgChangeList = []
netChange = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999999999999]

#sets path to be opened as a csvfile
with open(csvPath) as csvfile:
    csvReader = csv.reader(csvfile) #stores command to open the path
    header = next(csvReader) #skips the header
    firstRow = next(csvReader) #"skips" the first row to calc differences
    previousRow = int(firstRow[1]) #sets the first row as prev
    monthCount = 1 #sets prev it to 1 for the first row count
    netTotal = int(firstRow[1]) #sets initial value of the first row 

    #goes through each row in csv file
    for row in csvReader:

        #total num of months in dataset
        monthCount += 1

        #net amount
        netTotal += int(row[1])

        #avg change pt1: adds difference to a list
        changeCalculation = int(row[1]) - previousRow
        previousRow = int(row[1])
        avgChangeList.append(changeCalculation)

        #avg change pt2: calculating the sum of #'s in list / length
        finalAvgChange = sum(avgChangeList)/len(avgChangeList)
        
        #greatest increase calculation
        if changeCalculation > greatestIncrease[1]:
            greatestIncrease = [row[0],changeCalculation]

        #greatest decrease calculation
        if changeCalculation < greatestDecrease[1]:
            greatestDecrease = [row[0], changeCalculation]

        
# exporting analysis in text file
outputPath = os.path.join('Analysis', 'financial_analysis.txt')

with open(outputPath, 'w') as outputFile:
    outputFile.write("Financial Analysis\n")
    outputFile.write("----------------------------\n")
    outputFile.write(f"Total Months: {monthCount}\n")
    outputFile.write(f"Total: ${round(netTotal)}\n")
    outputFile.write(f"Average Change: ${round(finalAvgChange, 2)}\n")
    outputFile.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
    outputFile.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${round(netTotal)}")
print(f"Average Change: ${round(finalAvgChange,2)}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")