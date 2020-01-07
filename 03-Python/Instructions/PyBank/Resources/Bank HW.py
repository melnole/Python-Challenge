# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:26:29 2019

@author: mwilliamson
"""
#output is this:
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  
#  * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

#define variables
total = 0
averagepnl = 0   

bankcsv = os.path.join (r"Resources", "budget_data.csv")
bankcsv = r"C:\Users\mwilliamson\Desktop\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

#set integers, from classwork but i am not using for this one
     #months = int(bank_data[0])
     #pnl = int(bank_data[1])
     
#need to open text file to write to
budgetexport = open(r"C:\Users\mwilliamson\Desktop\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyBank\Resources\budgetexport.txt", "w+")

with open(bankcsv, newline="") as csvfile:
#header row thing, print it to make sure i have it correct
    csvheader = next(csvfile)
    #print(f"CSV header: {csvheader}")

#create lists to loop through and for appending    
    months = []    
    pnl = []

    for row in csvfile:
        #append rows to each other and add numbers in months to get total (adding to a list)
        months.append([row.split(",")[0],int(row.split(",")[1])])
        total = total + int(row.split(",")[1])

row = 1
while row < len(months):
    averagepnl = averagepnl + int(months[row][1])-int(months[row-1][1])
    # append changes to get pnl average
    pnl.append([str(months[row][0]),int(months[row][1])-int(months[row-1][1])])
    row += 1

totalmonths =len(months)
#print(totalmonths)
avgChange = averagepnl / (totalmonths -1)

biggestincrease = max(pnl)
biggestdecline = min(pnl)

biggestincreasenew = 0
biggestdeclinenew = 0

for currentrow in pnl:
  if int(biggestincreasenew) < int(currentrow[1]):
    biggestincreasenew = currentrow[1]
    bestmonth = currentrow[0]
  elif biggestdeclinenew > currentrow[1]:
    biggestdeclinenew = currentrow[1]
    worstmonth = currentrow[0]

#print (biggestincrease1)
#print (biggestdecline1)

print ('Financial Analysis')
print ('------------------------')
print (f'total months : {totalmonths}')
print (f'total : {total}')
print (f'average change : {avgChange}')
print (f'greatest profit increase : {bestmonth} : {biggestincreasenew}')
print (f'greatest profit decline: {worstmonth} : {biggestdeclinenew}')

budgetexport.write('Financial Analysis\n')
budgetexport.write('-----------------\n')
budgetexport.write('total months : {totalmonths}\n')
budgetexport.write('total : {total}\n')
budgetexport.write('averagechange : {avgChange}\n')
budgetexport.write('greatest profit increase : {bestmonth}\n')
budgetexport.write('greatest profit decline : {worstmonth}\n')


#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

    
    