# Team Narwhals (Mohtasim Howlader, Tania Cao Su)
# SoftDev1 pd8
# K10 -- Jinja Tuning
# 2018-09-24

import csv,random
from flask import Flask,render_template

app = Flask(__name__) #create instance of class Flask


@app.route("/")
def home():
    return "look at me,<br> <a href='/occupations'> go here </a>"

@app.route("/occupations")
def occ():
    createDict()
    ranOcc = chooseOccupation(occPerDict,perSum) #ranOcc is randomly chosen occupation
    return render_template("occ_display.html",
                            occVal = ranOcc,
                            dict = occPerDict, #dict in html is OccPerDict
                            )

occPerDict = {} #dictionary for occupations to percentage of U.S workforce is comprises
perSum = 0 #total sum of percentages of occupations, to be modified by createDict(), will become 99.8

#creates the dictionary of occupation percentages as occPerDict, also establishes perSum
def createDict():
    with open('occupations.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            # loops through each row of csv file
            for row in reader:
                    # checks to see that the total isn't added to the dictionary
                    if row['Job Class'] != "Total":
                           occPerDict[row['Job Class']] = float(row['Percentage'])
                    else:
                            global perSum
                            perSum = float(row['Percentage']) #the total percentage

#chooses a random occupation based on the percentage, d is the dictionary, totalSum is total Sum of percentages
def chooseOccupation(occDict,totalSum):

        occ = occDict.keys()
        weights = occDict.values() #weight is the same as percentage


        # generating a random number float from 0 to the total sum of the weights
        randWeight = random.uniform(0,perSum)

        i = 0 #variable to match occupation with its respective weight
        for weight in weights:
                #choosing the occupation if the randWeight created lies between the range of its weight.
                randWeight -= weight
                if randWeight <= 0:
                        break
                i+=1

        return list(occ)[i] # return random occupation

#Algorithm: a random float from 0 to the total percentage is generated using random.uniform and assigned to randWeight
#   use a for loop to iterate through the values of the dictionary (which represent the percentages or weights)
#   subtract a weight from the randWeight and increase i by 1 in each loop. When randWeight reaches 0, the for loop is broken.
#   return the occupation at index i from the list of occupations obtained from occDict.keys()

if __name__ == "__main__":
    app.debug = True
    app.run()
