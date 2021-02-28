from flask import Flask, request, render_template
import random, json, os

app = Flask(__name__)

jsonData = [
        {
            "eventName":"Birthday Party",
            "startDate":"",
            "endDate":"",
            "participants":"",
            "location":"",
            "budget":"",
            "suppliers":"",
            "eventDiscription":"some sort of discription for this amazing event that never took place"
        },
        {
            "eventName":"the second event",
            "startDate":"",
            "endDate":"",
            "participants":"",
            "location":"",
            "budget":"",
            "suppliers":"",
            "eventDiscription":"some sort of discription for this amazing event that never took place"
        },
        {
            "eventName":"the third event",
            "startDate":"",
            "endDate":"",
            "participants":"",
            "location":"",
            "budget":"",
            "suppliers":"",
            "eventDiscription":"some sort of discription for this amazing event that never took place"
        }
    ]

@app.route('/')
def homepage():
    """A homepage."""
    return render_template('home.html')

@app.route('/about')
def about():
    """About Page."""
    return render_template('about.html')

@app.route('/formList')
def formList():
    """Form list page"""
    return render_template('formList.html', jsonData=jsonData)

@app.route('/formList/<formName>')
def formPage(formName):
    """dynamic page for individual forms"""
    context = {
        'jsonData':jsonData,
        'formName':formName
    }
    return render_template('formPage.html', context=context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
