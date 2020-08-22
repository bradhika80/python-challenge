#*************************************************
# Student Name : Radhika Balasubramaniam
# Name : PyPoll python challenge
# Description : Create a Python script that analyzes the votes for a rural town
#**************************************************

#import the libraries

import os
import csv

# declare input file path
election_data = os.path.join("Resources", "election_data.csv")

# open csv file
with open(election_data) as csvfile:
    #read the file
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row 
    csv_header = next(csv_reader)

    #create a list of dictionary for candidates
    candidate_list_dictionary = dict()

    
    # ********* processing of the records in csv starts here *********
    for row in csv_reader:
        # retrieves the count value, if available, else returns 0

        candidate_count = candidate_list_dictionary.get(row[2])
        if candidate_count is None :
            count = 1
        else:
            count = candidate_count + 1
        
        candidate_list_dictionary.update({row[2] : count})


    print (candidate_list_dictionary)





   