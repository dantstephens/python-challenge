
# -----------------------------------------------------------------------------------------
# Import data from source CSV file
# -----------------------------------------------------------------------------------------

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

# -----------------------------------------------------------------------------------------
# Calculating total profit/loss and months
#
# Total profit/loss is calculated by summing the values in the profit/loss column
# Total months is calculated by adding 1 to a variable each time loop iteration
# -----------------------------------------------------------------------------------------
# Calculate monthly change
#
# Monthly change for each month is calculated by taking the current month value and 
# subtracting the previous month value the change is stored in an array. To get the average,
# we'll take the sum of the values in the array and divide it by the length(number of values)
# in the array.  
# -----------------------------------------------------------------------------------------
# Storing greatest and least change 
#
# To get the greatest increase and decrease, we'll include an if statement to check if each
# change value is greater than or less than the stored values. When a new value is stored, 
# the month also needs to be stored.
# -----------------------------------------------------------------------------------------


# declare variables and preset values 

    profloss_total = 0
    profloss_months = 0
    prev_month = 0
    max_change = 0
    min_change = 0
    change_list =[]

# starting loop to interate through each row
    for row in csvreader:

# calculating total profit/loss
        profloss_months = profloss_months + 1
        profloss_total = profloss_total + int(row[1])

# Calculating the monthly change if statement is used becuase we need to store a previous month
# value first before we begin calculating change.
        if prev_month != 0:
            change = int(row[1]) - prev_month 
            change_list.append(change)
            prev_month = int(row[1])

# If statements to capture and store least and greatest change
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
        else:
            prev_month = int(row[1])
        

# calculating the average change

average_change = sum(change_list) / len(change_list)

# rounding average change to 2 decimal points

average_change = round(average_change, 2)

# -----------------------------------------------------------------------------------------
# Print the final results the terminal
# -----------------------------------------------------------------------------------------

print(f'''
Financial Analysis
      
----------------------------
      
Total Months: {profloss_months}

Total: ${profloss_total}

Average Change: ${average_change}

Greatest Increase in Profits: {max_month} (${max_change})

Greatest Decrease in Profits: {min_month} (${min_change})    
      ''')
# -----------------------------------------------------------------------------------------
# Export the final results to a text file
# -----------------------------------------------------------------------------------------

output_path = os.path.join("analysis" ,"financial_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f'''
Financial Analysis
      
----------------------------
      
Total Months: {profloss_months}

Total: ${profloss_total}

Average Change: ${average_change}

Greatest Increase in Profits: {max_month} (${max_change})

Greatest Decrease in Profits: {min_month} (${min_change})    
      ''')


