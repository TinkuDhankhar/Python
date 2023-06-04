import requests
from bs4 import BeautifulSoup
#
# url = "https://nuusoftechnology.com"
# c = requests.get(url)
# print(c)
#
# soup = BeautifulSoup(c.content, "html.parser")
# t = soup.find_all('a')
# for a in t:
#     print(a.text)
#
# soup.find('div',class_="className")

for j in range(1,101):
    url = f"https://www.flipkart.com/search?q=dell&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={j}"
    response = requests.get(url)
    # print(response)
    html = BeautifulSoup(response.content,'html.parser')
    t = html.find_all("div",class_="_4rR01T")
    for i in t:
        print(i.text)

