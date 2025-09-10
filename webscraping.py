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