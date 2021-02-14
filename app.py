from flask import Flask, request, render_template
import random, json, os

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

# @app.route('/formList/<formName>')
# def formPage(formName):
#     """dynamic page for individual forms"""
#     with open('./static/jsonTestFiles/formData.json', 'r') as data:
#         jsonData = json.load(data)
#     for form in jsonData:
#         if form["eventName"] == {{formName}}:
#             storedForm = form
#     context = {
#         'storedForm': storedForm,
#         'jsonData': jsonData
#     }
#     print(jsonData)
#     return render_template('formPage.html', context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
