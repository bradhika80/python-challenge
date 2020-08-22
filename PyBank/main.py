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
    totalProfitLoses = 0.0
    previousProfitLoses = 0.0
    totalValueChanges =0.0
    
    #initialize the dictionary of the change values
    change_dictionary = dict()

    # ********* processing of the records in csv starts here *********
    for row in csv_reader:

        #calculate total profit values
        totalProfitLoses = float(row[1]) + totalProfitLoses

        # assign the first row value if its the first row
        if len(change_dictionary) < 1:
            previousProfitLoses = float(row[1])

        #calculate Valuechanges 
        totalValueChanges = (float(row[1]) - previousProfitLoses)  
        
        change_dictionary.update ( {row[0] : totalValueChanges} ) 

        #assign new profitLosesValue
        previousProfitLoses = float(row[1])

        
    # ********* processing of the records in csv ends here *********
       
    # calculation Analysis processing
        
    averageChange = sum(change_dictionary.values()) /(len(change_dictionary) - 1)

    #calculate the min and max value from the list
    max_key = max(change_dictionary, key=change_dictionary.get)
    min_key = min(change_dictionary , key=change_dictionary.get)


    # print the values in the console
    print()
    print("Financial Analysis")
    print("----------------------------")
    print()
    print(f"Total Months: {len(change_dictionary)}")
    print(f"Total: ${int(totalProfitLoses)}")
    print(f"Average  Change: ${round(averageChange, 2)}")
    print(f"Greatest Increase in Profits: {max_key} $({change_dictionary[max_key]})")
    print(f"Greatest Decrease in Profits: {min_key} $({change_dictionary[min_key]})")