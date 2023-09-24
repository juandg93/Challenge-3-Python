import csv

# Adjust the path for the election_data.csv
csv_path = "Resources/election_data.csv"

candidates = []

with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip header row
    next(csv_reader)
    
    for row in csv_reader:
        candidates.append(row[2])
total_votes = len(candidates)

# Count votes for each candidate
from collections import Counter
votes_counter = Counter(candidates)

# Determine the winner
winner = votes_counter.most_common(1)[0][0]
# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


output = "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += "-------------------------\n"

for candidate, votes in votes_counter.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

print(output)

with open("analysis/election_results.txt", 'w') as txt_file:
    txt_file.write(output)
