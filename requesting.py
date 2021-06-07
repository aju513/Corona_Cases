import requests

url = "https://covid-19-data.p.rapidapi.com/country"

querystring = {"name":"italy"}

headers = {
    'x-rapidapi-key': "a1980f425bmsh0893131aab4a581p1e9ad2jsn8ec0f61d4df5",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# country = data[0]['country']
# provinces=data[0]['provinces']
# province=data[0]['provinces'][0]['province']
# confirmed=data[0]['provinces'][0]['confirmed']
# recovered=data[0]['provinces'][0]['recovered']
# deaths=data[0]['provinces'][0]['deaths']
# active=data[0]['provinces'][0]['active']
