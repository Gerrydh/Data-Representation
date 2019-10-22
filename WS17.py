listings = soup.findAll("div", class_="PropertyListingCard" ) 

for listing in listings: 
    entry = [] 
    
    price = listing.find(class_="PropertyListingCard__Price").text 
    entry.append(price) 
    address = listing.find(class_="PropertyListingCard__Address").text 
    entry.append(address) 
    
    print(entry)