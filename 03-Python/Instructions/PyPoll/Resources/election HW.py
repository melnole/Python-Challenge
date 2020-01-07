# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:36:20 2019

@author: mwilliamson
"""
#You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  #The total number of votes cast
  #need list

  #A complete list of candidates who received votes
  #need list

  #The percentage of votes each candidate won
  
  #The total number of votes each candidate won

  #The winner of the election based on popular vote.

#need to loop through data
#need to gather total votes, total votes per candidate, percentage of votes per candidate, the max total votes per candidate and pull the name associated with the max
  

#output is this:

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

pollcsv = os.path.join (r"Resources", "election_data.csv")
pollcsv = r"C:\Users\mwilliamson\Desktop\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"
 
#need to open text file to write to
pollexport = open(r"C:\Users\mwilliamson\Desktop\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyPoll\Resources\pollexport.txt", "w+")

with open('pollcsv', newline='') as csvfile:

#reader and delimiter
     #csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
#header row thing, print it to make sure i have it correct
    csvheader = next(csvfile)
    #print(f"CSV header: {csvheader}"
    #get total votes by counting rows (votes are 1 per row)
    totalvotes=sum(1 for csvrow in csvfile)
    csvheader = next(csvfile)

#define lists
votes = []
candidates = []

for csvrow in csvfile:
        totalvotes = totalvotes + int(row.split(",")[1])













print ('Election Results')
print ('------------------------')
print (f'total votes : {totalvotes}')
print (f'greatest profit increase : {bestmonth}')
print (f'Winner: {xxx}')

budgetexport.write('Election Results')
budgetexport.write('-----------------\n')
budgetexport.write('total votes : {totalvotes}\n')
budgetexport.write('greatest profit increase : {bestmonth}\n')
budgetexport.write('Winner : {xxx}\n')