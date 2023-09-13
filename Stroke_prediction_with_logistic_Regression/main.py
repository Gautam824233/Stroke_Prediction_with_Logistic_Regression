# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template


app = Flask(__name__)
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
	return render_template("home.html")
# main driver function
if __name__ == '__main__':


	app.run(debug=True)