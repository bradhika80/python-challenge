import os
import csv

# declare input file path
budget_data = os.path.join("Resources", "budget_data.csv")

# open csv file
with open(budget_data) as csvfile:
    #read the file
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row 
    csv_header = next(csv_reader)

    #initialize variables
    totalMonths = 0
    totalProfitLoses = 0.0
    previousProfitLoses = 0.0
    totalValueChanges =0.0


    # ********* processing of the records in csv starts here *********
    for row in csv_reader:

        #store values
        totalMonths = totalMonths + 1
        totalProfitLoses = float(row[1]) + totalProfitLoses

        # assign the first row value if its the first row
        if totalMonths == 1:
            previousProfitLoses = float(row[1])

        #calculate Valuechanges 
        totalValueChanges = (float(row[1]) - previousProfitLoses) + totalValueChanges

        #assign new profitLoseValue
        previousProfitLoses = float(row[1])


         

    

    # calculation Analysis processing
        
    averageChange = totalValueChanges /(totalMonths -1)
    
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${int(totalProfitLoses)}")
    print(f"Average  Change: ${round(averageChange, 2)}")
