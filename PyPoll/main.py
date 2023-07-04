import os 
import csv

#path for file
csvPath = os.path.join('Resources','election_data.csv')

totalVotes = 0
voteDictionary = {}
greatestVotes = ['',0]
winnerName = greatestVotes[0]
winnerVote = greatestVotes[1]

with open(csvPath) as csvfile:
    csvReader = csv.reader(csvfile) #stores command to open the path
    header = next(csvReader) #skips the header

    #goes through each row in csv file
    for row in csvReader:

        #position row in candidate name found on col 3
        name = row[2]

        #total number of votes cast
        totalVotes += 1

        #list of candidates who received votes
        if name in voteDictionary:
            voteDictionary[name][0] += 1
        else:
            #adding candidate name, count value in a list 
            # we are later going to add a % to the list
            voteDictionary[name] = [1] 

    #calculating the percent of votes from total votes
    for name in voteDictionary:
        percent = (voteDictionary[name][0] / totalVotes) * 100
        voteDictionary[name].append(percent)

        #winner of the election based on popular vote
        if voteDictionary[name][1] > winnerVote:
            winnerName = name
            winnerVote = voteDictionary[name][1]
        
# exporting analysis in text file
outputPath = os.path.join('Analysis', 'voting_results.txt')

with open(outputPath, 'w') as outputFile:
    outputFile.write("Election Results""\n")
    outputFile.write("----------------------------""\n")
    outputFile.write(f"Total Votes: {totalVotes}""\n")
    outputFile.write("----------------------------""\n")
    for name in voteDictionary:
        outputFile.write(f"{name}: {round(voteDictionary[name][1], 3)}% ({voteDictionary[name][0]})""\n")
    outputFile.write("----------------------------""\n")
    outputFile.write(f"Winner: {winnerName}""\n")
    outputFile.write("----------------------------""\n")

#prints analysis in terminal
print("Election Results""\n")
print("----------------------------""\n")
print(f"Total Votes: {totalVotes}""\n")
print("----------------------------""\n")
for name in voteDictionary:
    print(f"{name}: {round(voteDictionary[name][1], 3)}% ({voteDictionary[name][0]})""\n")
print("----------------------------""\n")
print(f"Winner: {winnerName}""\n")
print("----------------------------""\n")

