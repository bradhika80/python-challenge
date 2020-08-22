#*************************************************
# Student Name : Radhika Balasubramaniam
# Name : PyPoll python challenge
# Description : Create a Python script that analyzes the votes for a rural town
#**************************************************

#import the libraries

import os as os
import csv as csv


# declare input file path
election_data = os.path.join("Resources", "election_data.csv")

# open csv file
with open(election_data) as csvfile:
    #read the file
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header row 
    csv_header = next(csv_reader)

    #create a dictionary for candidates
    candidate_dictionary = dict()
    totalVoteCount = 0

    
    # ********* processing of the records in csv starts here *********
    for row in csv_reader:  

        # retrieves the count value, if available, else returns none
        candidate_count = candidate_dictionary.get(row[2])
        
        # if the candidate_count is none, then its a new candidate hence count = 1, else add 1 to the existing count 
        if candidate_count is None :
            count = 1
        else:
            count = candidate_count + 1
        
        #insert/update the dictionary with  {"candidateName" : "updatedcountvalue"}
        candidate_dictionary.update ({row[2] : count})    
        totalVoteCount = totalVoteCount + 1
    
    # ********* processing of the records in csv ends here *********

    # winner key value
    winner_key = max(candidate_dictionary, key=candidate_dictionary.get)


     #********** build the output results in a list *********
    output_list = []
    output_list.append("")
    output_list.append("Election Results")
    output_list.append("----------------------------")
    output_list.append(f"Total Votes: {int(totalVoteCount)}")
    output_list.append("---------------------------------------")

    # iterating the candidate values in the dictionary
    for key in candidate_dictionary :
        value = candidate_dictionary[key]

        # format the percentage value with 3 places
        output_list.append(f"{key} : { format(round(float(value/totalVoteCount) * 100, 2), '.3f')}% ({value})")

    output_list.append("----------------------------")
    output_list.append(f"Winner: {winner_key} ")
    output_list.append("----------------------------")
  

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




    


   


