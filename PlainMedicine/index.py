from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def myMeds():
    return render_template('meds.html')

@app.route('/SignIn')
def singIn():
    return render_template('signIn.html')

@app.route('/SignUp')
def signUp():
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=1)