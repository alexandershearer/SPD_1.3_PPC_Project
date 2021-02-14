from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage."""
    return render_template('home.html')

@app.route('/formList')
def formList():
    """Form list page"""
    return render_template('formList.html')

# Dynamic page for individual forms
@app.route('/formList/<formName>')
def formPage(formName):
    """dynamic page for individual forms"""
    return render_template('formPage.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
