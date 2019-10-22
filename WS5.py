#print (soup.tr) 
rows = soup.findAll("tr") 

for row in rows: 
    print("------") 
    print(row)