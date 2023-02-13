import os
import csv
#import csv file
csvpath = os.path.join("Resources","election_data.csv")

#identify voter list and candidate's dictionary
number_vote = []
candidates = dict()

#open and read csv file 
with open(csvpath,'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader) #skip the header
    #loop through the data and get number of candidates with their total votes
    for row in csvreader:
        number_vote.append(row[0])
        candidate = row[2]
        
        if candidate not in candidates.keys():
            candidates.update({candidate:0})   # update new candidate into dict
        candidates[candidate] += 1     # add up total votes for each candidate

#calculate total votes
total_votes = sum(candidates.values())
#calculate final winner
winner = max(candidates, key=lambda k: candidates[k])

# Print the results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {len(number_vote)}")
print(f"----------------------------")
for x in candidates:
    print(f"{x}:, {(candidates[x]/total_votes*100):.3f}%({candidates[x]})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")


# create a open output file
output_file = os.path.join("election_final.csv")
with open(output_file, "w") as file:
    writer = csv.writer(file)

    # Write the header row
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(number_vote)}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    for x in candidates:   
        file.write(f"{x}:, {(candidates[x]/total_votes*100):.3f}%({candidates[x]})")
        file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")
