#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/activity")

#‘/’ URL is bound with first_flask function.
def first_flask():
    n = "Ricky"
    return render_template('index.html', name = n)

#run the application on local server
app.run(debug = True)
