for row in rows: 
    
    #print(row) 
    cols = row.findAll("td") 
    
    for col in cols: 
        print(col.text)