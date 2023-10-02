# -----------------------------------------------------------------------------------------
# Import data from source CSV file
# -----------------------------------------------------------------------------------------

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

# -----------------------------------------------------------------------------------------
# Counting candidate votes
#
# Candidate votes are calculated using conditional values to check for candidate names
# and adds to each candidates tally. An additional tally is kept for total votes across
# all candidates. 
# -----------------------------------------------------------------------------------------

# declare variables and preset values

    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
    total_votes = 0

# starting loop to interate through each row
    for row in csvreader:
        total_votes = total_votes + 1

# condidtional statements to check for candidate votes
        if row[2] == "Charles Casper Stockham":
            stockham_votes = stockham_votes + 1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes = doane_votes + 1
        elif row[2] == "Diana DeGette":
            degette_votes = degette_votes + 1

# calculate percentage of votes for each candidate and convert to rounded percentages

stockham_percent = (stockham_votes / total_votes) * 100
stockham_percent = round(stockham_percent, 3)
doane_percent = (doane_votes / total_votes) * 100
doane_percent = round(doane_percent, 3)
degette_percent = (degette_votes / total_votes) * 100
degette_percent = round(degette_percent, 3)

# conditional statement to determine winner

if stockham_votes > doane_votes and stockham_votes > degette_votes:
    winner = "Charles Casper Stockham"
elif doane_votes > stockham_votes and doane_votes > degette_votes:
    winner = "Raymon Anthony Doane"
elif degette_votes > stockham_votes and degette_votes> doane_votes:
    winner = "Diana DeGette"

# -----------------------------------------------------------------------------------------
# Print the final results the terminal
# -----------------------------------------------------------------------------------------

print(f'''
Election Results

-------------------------

Total Votes: {total_votes}

-------------------------

Charles Casper Stockham: {stockham_percent}% ({stockham_votes})

Diana DeGette: {degette_percent}% ({degette_votes})

Rayman Anthony Doane: {doane_percent}% ({doane_votes})

-------------------------

Winner: {winner}

-------------------------
      ''')

# -----------------------------------------------------------------------------------------
# Export the final results to a text file
# -----------------------------------------------------------------------------------------

output_path = os.path.join("analysis" ,"election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f'''
Election Results

-------------------------

Total Votes: {total_votes}

-------------------------

Charles Casper Stockham: {stockham_percent}% ({stockham_votes})

Diana DeGette: {degette_percent}% ({degette_votes})

Rayman Anthony Doane: {doane_percent}% ({doane_votes})

-------------------------

Winner: {winner}

-------------------------
      ''')
