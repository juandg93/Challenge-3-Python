import csv

# Create a path to the budget_data.csv in the Resources folder
csv_path = "Resources/budget_data.csv"

# Initialize lists to store data
dates = []
profits_losses = []

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip header row
    next(csv_reader)
    
    for row in csv_reader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))
        # The total number of months included in the dataset
total_months = len(dates)
total_profit_loss = sum(profits_losses)

# The net total amount of "Profit/Losses" over the entire period
changes = [profits_losses[i+1] - profits_losses[i] for i in range(len(profits_losses)-1)]
average_change = sum(changes) / len(changes)

greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)+1]

greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)+1]
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
)

print(output)

with open("analysis/results.txt", 'w') as txt_file:
    txt_file.write(output)
