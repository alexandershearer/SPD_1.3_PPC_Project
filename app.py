from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage."""
    return render_template('home.html')

@app.route('/formPage')
def formPage():
    """Page1."""
    return render_template('formPage.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
