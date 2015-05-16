from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)

@app.route('/')
def myMeds():
    return render_template('meds.html', data=getMeds())

def getMeds():
	req = urllib.request.Request('http://lyfjaver.is/lyfjaskra')
	response = urllib.request.urlopen(req)
	bsoup = BeautifulSoup(response)
	tables = bsoup.findAll('td', {'class': 'row1'})

	return tables

@app.route('/SignIn')
def singIn():
    return render_template('signIn.html')

@app.route('/SignUp')
def signUp():
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=1)
