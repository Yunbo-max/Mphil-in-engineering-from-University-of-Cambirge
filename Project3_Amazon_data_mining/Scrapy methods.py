from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_title(soup):
    try:     
        title = soup.find("span", attrs={"id": 'productTitle'})    
        title_value = title.string    
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


def get_price(soup):
    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()

    except AttributeError:

        try:
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price


def get_rating(soup):
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:

        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count


def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available

def rank(soup):
    try:
        review_count = soup.find("span", attrs={'class': 'a-list-item'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

if __name__ == '__main__':
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.amazon.co.uk',
        'Referer': 'https://www.amazon.co.uk/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    page = 1
    while page != 2:
        URL = f"https://www.amazon.co.uk/Best-Sellers-Fashion-Womens-Bra-Minimizers/zgbs/fashion/14072537031/ref=zg_bs_pg_1?_encoding=UTF8&pg={page}"
        webpage = requests.get(URL, headers=headers)
        soup = BeautifulSoup(webpage.content, "lxml")
        links = soup.find_all("a", attrs={'class': 'a-link-normal'})
        links_list = []

        for link in links:
            links_list.append(link.get('href'))
        item_details = []
        for link in links_list:
            new_webpage = requests.get("https://www.amazon.co.uk" + link, headers=headers)

            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            data = {
                                "Product Title":get_title(new_soup),
                                "Product Rating":get_rating(new_soup),
                                "Number of Product Reviews":get_review_count(new_soup),
                                "Amazon Rank":rank(new_soup),
                                'Sales':get_sales(new_soup),
                                'Product Price':get_price(new_soup)
                            }
            item_details.append(data)
        dataframe = pd.DataFrame()
        dataframe = dataframe.append(item_details,ignore_index=True)
        print(dataframe)
        page = int(page) + 1
        MenOverall_csv_data = dataframe.to_csv('women_bra.csv', index=True)
