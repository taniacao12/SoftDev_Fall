# BlueOrange -- Tania Cao, Jack Lu
# SoftDev1 pd8
# K06 -- StI/O: Divine your Destiny!
# 2018-09-13

import csv
import random

# Chooses random occupation based on percentage of US workforce comprised of it.
def choose(fileName):

    # Builds a dictionary of careers occupations and percentage of US workforce.
    dict = {}
    with open(fileName, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        heading = reader.__next__() # skips column labels Job Class, Percentage
        for i in reader:
            dict[ i[0] ] = float( i[1])
        del dict['Total'] # Deletes total percentage

    jobs = list(dict.keys()) # Created a list of keys to support indexing.

    # Chooses a job using corresponding values as relative weights. [0] because random.choices returns a list.
    fate = random.choices(jobs, dict.values())[0]

    return fate

print("You shall work in " + choose('occupations.csv') + " for the rest of your life.")
