# The site I am using for this Lab is the Kohls Retail Site
# In specific, the prodcut I am scraping for is Dolce & Gabbana Light Blue Cologne

import requests, re
from bs4 import BeautifulSoup

# The URL of the site and the item I am looking for
URL = requests.get("https://www.kohls.com/product/prd-4357812/light-blue-pour-homme-eau-de-toilette.jsp?prdPV=2").content
# using HTML parser
soup = BeautifulSoup(URL, 'html.parser')


#findItem as my command to find the item name
#using itemName as the variable for storing the name of the product
findItem = soup.find("h1", {"class":"product-title"})
itemName = findItem.text


#findPrice as my command to find the item price
#itemPrice as my variable to store the price
findPrice = soup.find("span", {"class":"pdpprice-row2-main-text"})
itemPrice = findPrice.text

#display the item name and item price 
print("The price of %s is %s" % (itemName, itemPrice))


#example of how it diplays: "The price of DOLCE&GABBANA Light Blue Pour Homme Eau de Toilette is 57.00-125.00
