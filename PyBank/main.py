
#*************************************************
# Student Name : Radhika Balasubramaniam
# Name : PyBank python challenge
# Description : Creating a Python script for analyzing the financial records of your company
#**************************************************

#import the libraries

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

        #calculate total profit/loss values
        totalProfitLoses = float(row[1]) + totalProfitLoses

        # assign the first row value if its the first row, since the change should be set to zero
        if len(change_dictionary) < 1:
            previousProfitLoses = float(row[1])

        #calculate Valuechanges 
        totalValueChanges = (float(row[1]) - previousProfitLoses)  
        
        #add the values to dictionary {"Datevalue" : "changevalue"}
        change_dictionary.update ( {row[0] : totalValueChanges} ) 

        #assign new profitLosesValue
        previousProfitLoses = float(row[1])

        
    # ********* processing of the records in csv ends here *********
       
    # calculation Analysis processing
    
    #average change = sum of the change values in directory/ length of dictionary -1 (first month has to be removed since change would be zero)
    averageChange = sum(change_dictionary.values()) /(len(change_dictionary) - 1)

    #calculate the min and max value from the list
    max_key = max(change_dictionary, key=change_dictionary.get)
    min_key = min(change_dictionary , key=change_dictionary.get)

   
   #********** build the output results in a list *********
    output_list = []
    output_list.append("")
    output_list.append("Financial Analysis")
    output_list.append("----------------------------")
    output_list.append("")
    output_list.append(f"Total Months: {len(change_dictionary)}")
    output_list.append(f"Total: ${int(totalProfitLoses)}")
    output_list.append(f"Average  Change: ${round(averageChange, 2)}")
    output_list.append(f"Greatest Increase in Profits: {max_key} $({change_dictionary[max_key]})")
    output_list.append(f"Greatest Decrease in Profits: {min_key} $({change_dictionary[min_key]})")

    #********** build the output results completed *********

    # printing the output to console by iterating through the list 

    for msg in output_list :
        print (msg) 
    
    # printing to console is completed

    # printing the output to file

    #build outfile path
    out_path = os.path.join("Analysis", "output.txt")

    #create a new output file
    with open(out_path, 'w') as outputFile:
        for msg in output_list :
            outputFile.writelines(msg + "\n")

    # printing the output to file is completed





   