from __future__ import division
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    instructions1 = "If you have an account please Login below."
    instructions2 = "If you don't have an account please create one from the Dropdown Menu."
    return render_template('index.html', instructions1=instructions1, instructions2=instructions2)

@app.route('/singin')
def singin():
    return render_template('singin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/form', methods=['POST', 'GET'])
def form():

    if request.method == "POST":
        username = request.form["Username"]

        if not username:
            show_error = "You need to fill out the forms required. Please try again."
            return render_template("fail.html", show_error=show_error)

        try:
            return redirect('/form')

        except:
            return "There was an error! Please try again."

    else:
        return render_template('form.html')


transactions = []

@app.route('/Info', methods=['POST', 'GET'])
def Info():
    first_name = request.form.get("first_name")
    middle_name = request.form.get("middle_name")
    last_name = request.form.get("last_name")
    fathers_name = request.form.get("fathers_name")
    mothers_name = request.form.get("mothers_name")
    return render_template('Info.html', first_name=first_name, middle_name=middle_name,last_name=last_name,fathers_name=fathers_name,mothers_name=mothers_name)

""""@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == "POST":
        beta = float(request.form.get("Power"))
        alpha = float(request.form.get("Alpha"))
        x1 = float(request.form.get("M1"))
        x2 = float(request.form.get("M2"))
        s1 = float(request.form.get("S1"))
        s2 = float(request.form.get("S2"))

    zbeta = st.norm.ppf(1 - beta)
    zalpha = st.norm.ppf(1 - alpha / 2)
    n = (math.pow((zalpha + zbeta), 2) * (math.pow(s1, 2) + math.pow(s2, 2))) / (math.pow((x1 - x2), 2))
    return render_template('calculate.html', beta=beta, alpha=alpha, x1=x1, x2=x2, s1=s1, s2=s2, n=n)"""



"""
    #zbeta = st.norm.ppf(1 - beta)
    #zalpha = st.norm.ppf(1 - alpha / 2)

    #n = (math.pow((zalpha + zbeta), 2) * (math.pow(s1, 2) + math.pow(s2, 2))) / (math.pow((x1 - x2), 2))
    return render_template('calculate.html')"""