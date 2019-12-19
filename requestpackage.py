import requests
#url = 'https://www.gmit.ie'


#response = requests.get(url)

#print(response.status_code)
#print(response.text)
#print(response.headers)

url = 'http://127.0.0.1:5000/cars'
data = {'reg':'201D258', 'make': 'Bently', 'model': 'Phantom', 'price':256325}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())