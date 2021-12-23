from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secrets don't make friends"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/route')
def atoute():
	pass

@app.route('/route')
def atoute():
	pass

@app.route('/route')
def atoute():
	pass

# no page found
@app.errorhandler(404)
def pageNotFound(missing):
	return "Sorry! No response. Try again."

if __name__=="__main__":
	app.run(debug=True)