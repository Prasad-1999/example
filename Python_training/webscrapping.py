# To create website by using python
import requests
import pandas
from bs4 import BeautifulSoup

# To send the request to websit
response = requests.get("https://www.bikewale.com/")
# print(response) # To know reponse
soup = BeautifulSoup(response.content, 'html.parser')  # To know about content
# print(soup) #To see about content
names = soup.find_all('a', title="Hero HF Deluxe")  # to know about names
name = []  # To store the names of products
for i in names[1]:
    d = i.get_text()  # to get the text information
    name.append(d)  # Add the names
# print(name)  # To print names

prices = soup.find_all('span', class_="font18")  # to know about prices
price = []  # To store the names of products
for i in prices[1]:
    d = i.get_text()  # to get the text information
    price.append(d)  # Add the prices
# print(price)  # To print prices

data = {'Names': name, 'prices': price}
# print(data) #To print data of website
df = pandas.DataFrame(data)
# print(df) #To data in rows and columns
df.to_csv("bike_data.csv")
