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

    




   