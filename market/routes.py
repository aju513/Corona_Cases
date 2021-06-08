from market import app
from flask import request,render_template
from pip._vendor import requests
@app.route('/homepage',methods=['POST','GET'])
def homepage():
	
	
	url = "https://covid-19-data.p.rapidapi.com/totals"

	headers = {
		'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
		'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
		}

	response = requests.request("GET", url, headers=headers)
	data=response.json()
	confirmed_total= data[0]['confirmed']
	recovered_total = data[0]['recovered'] 
	deaths_total = data[0]['deaths']

	if request.method=="POST":

		 
		country_name=request.form['code']
	  	
		url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

		querystring = {"country":country_name}

		headers = {
			'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
			'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    			}

		response = requests.request("GET", url, headers=headers, params=querystring)
		data=response.json()
		status=data['data']['covid19Stats']
		return render_template('homepage.html',temp=status,confirmed=confirmed_total,recovered=recovered_total,deaths=deaths_total)
	else:

		return render_template('homepage.html',confirmed=confirmed_total,recovered=recovered_total,deaths=deaths_total)

 
	