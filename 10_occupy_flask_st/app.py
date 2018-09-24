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
    ranOcc = chooseOccupation(occPerDict,perSum) #randomly chosen occupation as a string
    return render_template("occ_display.html",
                            occVal = ranOcc,
                            dict = occPerDict,
                            job = occ
                            )


#Write a Flask app with an "/occupations" route, which will generate an HTML page with an appropriate title,
#a descriptive heading, and a table-ified version of the occupations data, along with a a randomly selected occupation shown at the top.
#generate html file
#
#returns random occupation based on percent of likelihood

occPerDict = {}
perSum = 0 #total sum of percentages of occupations, to be modified by createDict()

#creates the dictionary of occupation percentages to occPerDict, also established totalSum
def createDict():
    with open('occupations.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            # eliminates first row of csv file
            next(reader)
            # loops through each row of csv file
            for row in reader:
                    # checks to see that the total isn't added to the dictionary
                    #print (row['Job Class'])
                    if row['Job Class'] != "Total":
                           occPerDict[row['Job Class']] = float(row['Percentage'])
                    else:
                            global perSum
                            perSum = float(row['Percentage'])
                            #print (perSum)

#chooses a random occupation based on the percentage, d is the dictionary, totalSum is total Sum of percentages
def chooseOccupation(d,totalSum):
        i = -1 #variable to match occupation with its respective weight
        occ = d.keys()
        weights = d.values()

        # generating a random number float from 0 to the total sum of the weights
        #print (total)
        randWeight = float(random.randrange(0,(int)(perSum*100)))/100 #range from 0 to totalSum
        #print (randWeight)

        for weight in weights:
                #choosing the occupation if the randWeight created lies between the range of its weight.

                randWeight -= weight
                if randWeight <= 0:
                        break
                i+=1
                #print(i)
        #print (i)
        #print (len(list(weights)))
        return list(occ)[i]



if __name__ == "__main__":
    app.debug = True
    app.run()
