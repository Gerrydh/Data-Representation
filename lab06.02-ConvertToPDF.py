import requests
import json

#html = '<h1> hello, world</h1>This is HTML'

f = open("../carviewer.html", "r")
html = f.read()

apikey = '8c0e5202752a9f00b139b7d0f36bd79f75741975'
url = 'https://api.html2pdf.app/v1/generate'

#putting the API Key in as data

data = {'html': html, 'apikey': apikey}
response = requests.post(url, json=data)

newFile = open("lab06.02.htmlaspdf.pdf", "wb")
newFile.write(response.content)
print(response.status_code)