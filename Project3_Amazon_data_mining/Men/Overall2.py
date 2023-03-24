from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

time.sleep(5)

amazon_url = "https://www.amazon.co.uk/Best-Sellers-Fashion-Mens-Underwear/zgbs/fashion/1731031031/ref=zg_bs_pg_2?_encoding=UTF8&pg=2"


page = requests.get(amazon_url)
soup = BeautifulSoup(page.content, 'html.parser')

div_tag = soup.find_all('div', attrs={'class': '_cDEzb_p13n-sc-css-line-clamp-3_g3dy1'})
span_tag1 = soup.find_all('span', attrs={'class': 'a-icon-alt'})
span_tag2 = soup.find_all('span', attrs={'class': 'a-size-small'})
span_tag3 = soup.find_all('span', attrs={'class': '_cDEzb_p13n-sc-price_3mJ9Z'})
span_tag4 = soup.find_all('span', attrs={'class': 'zg-bdg-text'})


Name = []
Review_score = []
Review_number = []
Price = []
Rank = []

for element in div_tag:
    Name.append(element.get_text())

for element in span_tag1:
    Review_score.append(element.get_text())

for element in span_tag2:
    Review_number.append(element.get_text())

for element in span_tag3:
    Price.append(element.get_text())

for element in span_tag4:
    Rank.append(element.get_text())



print(Name)
print(Review_score)
print(Review_number)
print(Price)
print(Rank)

Rank.pop(16)
Review_number.pop()
Review_number.pop()
print(len(Name))
print(len(Review_score))
print(len(Review_number))
print(len(Price))
print(len(Rank))


data=pd.DataFrame({'Name':Name,'Review_score':Review_score,'Review_number':Review_number, 'Rank':Rank})

print(data)

MenOverall_csv_data = data.to_csv('Men_Overall2.csv', index = True)
print(MenOverall_csv_data)

