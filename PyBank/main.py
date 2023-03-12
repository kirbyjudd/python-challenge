import os
import csv

budgetcsv = os.path.join("Resources", "budget_data.csv")

# variables for counting total months, net profit/losses, two lists to append changes and dates, and variables to hold the current and previous month values
count_months = 0
net_profit_losses = 0

changes = []
dates = []

current_month_value = 0
previous_month_value = 0

with open(budgetcsv, "r", encoding="utf8") as csvFile:

    csvreader = csv.reader(csvFile, delimiter=",")

    # stores the csv header row into 'csv_header'
    csv_header = next(csvreader)

    # the first row read gives us our initial starting month value and net profit/losses
    first_row = next(csvreader)
    previous_month_value = int(first_row[1])
    count_months += 1
    net_profit_losses += int(first_row[1])
    

    # for loop to go through each row and count the month, calcualte the net profit/losses, and calculate the change in value from the current and previous months
    for row in csvreader:
        count_months += 1
        current_month_value = int(row[1])
        net_profit_losses += current_month_value
        value_change = current_month_value - previous_month_value

        # appends the value change calculation to the changes list
        changes.append(value_change)

        # sets the previous month value to equal the new current month value
        previous_month_value = current_month_value

        # appends the current date to the dates list
        dates.append(row[0])

    # calculates the average, max, and min profit/losses from the changes list
    avg_profit_losses = round(sum(changes)/(count_months - 1), 2)
    max_profit_losses = max(changes)
    min_profit_losses = min(changes)

    # prints the results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${net_profit_losses}")
    print(f"Average Change: ${avg_profit_losses}")
    print(f"Greatest Increase in Profits: {dates[changes.index(max_profit_losses)]} (${max_profit_losses})")
    print(f"Greatest Decrease in Profits: {dates[changes.index(min_profit_losses)]} (${min_profit_losses})")

# writes and exports the results to a text file called "financial_output.txt" located in the analysis folder
financial_output = os.path.join("analysis", "financial_output.txt")
with open(financial_output, "w", encoding="utf8") as textFile:

    textFile.write("Financial Analysis\n")
    textFile.write("----------------------------\n")
    textFile.write(f"Total Months: {count_months}\n")
    textFile.write(f"Total: ${net_profit_losses}\n")
    textFile.write(f"Average Change: ${avg_profit_losses}\n")
    textFile.write(f"Greatest Increase in Profits: {dates[changes.index(max_profit_losses)]} (${max_profit_losses})\n")
    textFile.write(f"Greatest Decrease in Profits: {dates[changes.index(min_profit_losses)]} (${min_profit_losses})\n")
