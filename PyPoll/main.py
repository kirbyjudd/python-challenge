import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# variables for counting total votes
# also a list to append candidates names and a dictionary for votes and candidate names (keys: Names, values: votes)
count_votes = 0
candidates = []
votes_and_names = {}

with open(election_csv, "r", encoding="utf8") as csvFile:

    csvreader = csv.reader(csvFile, delimiter=",")

    # stores the csv header row into 'csv_header'
    csv_header = next(csvreader)

    # for loop goes through each row to calculate the total count of votes
    for row in csvreader:
        count_votes += 1

        # if candidate name is not in the candidates list, then add the name to the candidates list and to the votes_and_names dictionary
        if row[2] not in candidates:
            candidates.append(row[2])
            votes_and_names [row[2]] = 0

        # count votes for each individual candidate
        votes_and_names [row[2]] += 1

    # calculate the winner by getting the max vote values (popular vote) and the index for the winner name
    winner = max(zip(votes_and_names.values(), votes_and_names.keys()))[1]

    # prints the election results to the terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {count_votes}")
    print("----------------------------")

    # for loop that uses the keys and values in the votes_and_names dictionary to print out each candidate name, calculated percentage of votes, and total votes
    for key, values in votes_and_names.items():
        percentage = (values/count_votes)*100
        print(f"{key}: {percentage :.3f}% ({values})")

    # print out the winner's name (base on the winner calculation above)
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

# writes and exports the results to a text file called "election_results.txt" located in the analysis folder
election_results = os.path.join("analysis", "election_results.txt")
with open(election_results, "w", encoding="utf8") as textFile:

    textFile.write("Election Results\n")
    textFile.write("----------------------------\n")
    textFile.write(f"Total Votes: {count_votes}\n")
    textFile.write("----------------------------\n")
    for key, values in votes_and_names.items():
        percentage = (values/count_votes)*100
        textFile.write(f"{key}: {percentage :.3f}% ({values})\n")
    textFile.write("----------------------------\n")
    textFile.write(f"Winner: {winner}\n")
    textFile.write("----------------------------\n")