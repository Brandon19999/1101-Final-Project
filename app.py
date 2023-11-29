# import libraries and packages, they contain additional functions.

from flask import Flask, render_template


#create web application usin Flask
app = Flask(__name__)

#create our routes
@app.route('/')
def home():
 return render_template('index.html')

#start the web application 
app.run(
 debug=True
)