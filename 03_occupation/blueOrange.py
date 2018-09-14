import random

def occupation (fileName):
    import csv
    list = []
    count = 0
    file = open (fileName, 'r')
    content = csv.reader (file)
    for line in content:
        if line[0] != 'Job Class' and line[0] != 'Total':
            while count != float(line[1]):
                list.append(line[0])
                count += 0.1
            count = 0
    file.close ()
    print(list)
    return random.choice(list)
print(occupation('occupations.csv'))