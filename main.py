from flask import Flask,request,render_template
import requests

app=Flask(__name__)
 



@app.route('/',methods=['POST','GET'])
def homepage():
	if request.method=="POST":
		country_name=request.form['code']
	 
		url = "https://covid-19-data.p.rapidapi.com/country" 
		querystring = {"name":country_name}

		headers = {
		    'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
		    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)
		 
		data=response.json()
		country=data[0]['country']
		
		confirmed= data[0]['confirmed']
		recovered = data[0]['recovered']
		critical = data[0]['critical']
		deaths = data[0]['deaths']
		 
		 
		          
	
		# return render_template('data.html',country=country,confirmed=confirmed,recovered=recovered,critical=critical,deaths=deaths)
		return render_template('data.html',temp=data,country=country,confirmed=confirmed,recovered=recovered,critical=critical,deaths=deaths)
	else:

		return render_template('homepage.html')

 

if __name__=='__main__':
	app.run(debug=True)


