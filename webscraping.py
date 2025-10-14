from bs4 import BeautifulSoup

html="""<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were</p>
<div>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</div>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.

<p class="story">...</p>
"""

parser=BeautifulSoup(html,"html.parser")
print(parser.prettify())
# title gives title tag
parser.title
parser.a
parser.findAll("a")
print(parser.find_all_previous("a"))



import requests
from bs4 import BeautifulSoup

url="https://www.candere.com/gold-rate-today/tamilnadu"
url_data=requests.get(url)
# url_data.text
# print(url_data)
soup=BeautifulSoup(url_data.text,"html.parser")
soup.get_text()
soup.prettify
list_rate=soup.find_all("p",class_="goldCard--rate")
list_karat=soup.find_all("p",class_="goldCard--karat")
gold_data={
    list_karat[0]:list_rate[0],
    list_karat[1]:list_rate[1]
}
print("""\tThe Gold details\t\n\t karat->{0} : rate->{1} , karat->{2} : rate->{3}""".format(list_karat[0].text,list_rate[0].text,list_karat[1].text,list_rate[1].text))
# print()


import requests
from bs4 import BeautifulSoup

url = "https://www.livegoldrate.co.in/silver-prices/today-silver-rate-in-tamil-nadu/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
url_data = requests.get(url, headers=headers)
soup = BeautifulSoup(url_data.text, "html.parser")
print
silver_rows = soup.find_all("tr")
silver_rows.remove(silver_rows[0])  # Remove header row if present
if silver_rows:
    for row in silver_rows:
        cols = row.find_all("td")
        print(cols)
        if len(cols) >= 2:
            print(f"Silver Rate: {cols[0].text.strip()} - {cols[1].text.strip()}")
else:
    print("Silver rate data not found or page structure changed.")
# print()

# new code

import requests
from bs4 import BeautifulSoup
url = "https://www.bikewale.com/best-scooters-in-india/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)  # Debug: Check if request was successful
soup = BeautifulSoup(response.text, "html.parser")

scooter_names = soup.find_all("li", class_="o-em o-hk")
for scooter in scooter_names:
    print
    vehicle_name=scooter.find("h3").text.strip()
    vehicle_price=scooter.find("span",class_="o-f").text.strip()
    print(f"Vehicle Price:{vehicle_price} \nVehicle Name: {vehicle_name}",end="\n\n")
    print(f"Vehicle Name: {vehicle_name}")

# new code


import requests     
from bs4 import BeautifulSoup

url = "https://www.bikewale.com/best-scooters-in-india/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)       
print("Status Code:", response.status_code)  # Debug: Check if request was successful
soup = BeautifulSoup(response.text, "html.parser")      
scooter_names = soup.find_all("li", class_="o-em o-hk")    
for scooter in scooter_names:
    print()





import requests     
from bs4 import BeautifulSoup

url = "https://www.accuweather.com/en/za/durban/305605/hourly-weather-forecast/305605"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.text, "html.parser")   
out_1=soup.find("div",class_="panel no-realfeel-phrase")
out_2=out_1.find_all("p")
# out_2[1].text
out_1=out_1.find("p")
out_2=out_1.find_next_sibling("p")
print(out_2.text)



import requests     
from bs4 import BeautifulSoup

url = "https://www.emirates.com/in/english/book/featured-fares/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.text, "html.parser")
fare_divs_eco=soup.find("span",class_="feature-fare-cabin-tabs__price-text") 
fare_divs_eco.text.strip("*")
fare_divs_bus = soup.find("div", class_=[
    "feature-fare-cabin-tabs__active_class_code_J"
    "feature-fare-cabin-tabs__cabins",
    "feature-fare-cabin-tabs__multi_cabins",
])
fare_divs_bus_span=fare_divs_bus.find("span",class_="feature-fare-cabin-tabs__price-text")
fare_divs_bus_span.text.strip("*")
# for fare in fare_divs:
#     print(fare.text)



