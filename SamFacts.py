#import some libraries
import sys
from random import randint

#open the file containing my qualifications
with open("Sam_deJong.dat") as f:
    Facts = f.readlines()
    
#clear whitespace and remove empty entries
Facts = [x.strip() for x in Facts] 
Facts = [s for s in Facts if len(s) != 0]



print "I am the highly qualified, well rounded candidate that you're looking for!"


numFacts=""
#loop until a positive number is entered
while not numFacts.isdigit():
    
    #get user input
    numFacts = raw_input("Enter a number to see a few of my qualities:")
        
    #if not a number, print a message
    if not numFacts.isdigit():
        print "Not a number!"
        
#print a message if no facts requested
if int(numFacts) == 0:
    print "Ok, lets talk in person instead! Call me at 250-888-5720 to set up an interview!"
    quit()
    

#if there's more facts requested than the file contains, print all the facts,
tooMany=False
if int(numFacts) > len(Facts):
    numFacts = len(Facts)
    tooMany=True


print "I am:"

#print randomly selected facts
randomNums = list()
while len(randomNums) < int(numFacts):
    rNum =  randint(0, len(Facts)-1)

    #make sure there's no doubles
    if rNum not in randomNums:
        randomNums.extend([rNum])
        thisFact = Facts[rNum]
        
        #do some formatting (add A or An in front of the fact)
        precurser = "\tA "
        if thisFact[0] in ('a', 'e', 'i', 'o', 'u'):  #at 'An' if the fact starts with a vowel
            precurser="\tAn "
        if thisFact[0] == 'Y':  #special case
            precurser = "\t"
        if thisFact[:3] == "The": #special case
            precurser = "\t"
        print precurser+thisFact
        
#if more facts are requested than the file contains, print info for getting more
if tooMany:
    print "To hear more, call me at 250-888-5720"
        



