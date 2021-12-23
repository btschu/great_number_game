from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secrets don't make friends"

@app.route('/')
def index():
    if 'randomNum' in session:
        pass
    else:
        session['randomNum'] = random.randint(1,100)
    if 'numTries' in session:
        pass
    else:
        session['numTries'] = 0
    if 'guess' in session:
        pass
    else:
        if request.form.get('guess'):
            session['guess'] = int(request.form['guess'])
        else:
            session['guess'] = -1
    return render_template("index.html")

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect("/")

@app.route('/guess', methods=['POST'])
def guess():
    if 'numTries' in session:
        session['numTries'] += 1
    else:
        session['numTries'] = 0
    session['guess'] = int(request.form['guess'])
    session['randomNum'] = int(session['randomNum'])
    return redirect("/")

# no page found
@app.errorhandler(404)
def pageNotFound(missing):
	return "Sorry! No response. Try again."

if __name__=="__main__":
	app.run(debug=True)