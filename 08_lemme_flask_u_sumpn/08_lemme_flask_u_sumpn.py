# Tania Cao
# SoftDev1 pd8
# K8 -- Fill Yer Flask
# 2018-09-19

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def index():
    print('The module is ')
    print(__name__)
    return '/ ----> index <br> /fact ----> fact <br> /name ----> name'

@app.route('/fact')
def fact():
    return 'Fun Fact: The world’s oldest piece of chewing gum is over 9,000 years old!'
    
@app.route('/name')
def name():
    return 'My name is Tania.'
    
if __name__ == '__main__':
    app.debug = True
    app.run()