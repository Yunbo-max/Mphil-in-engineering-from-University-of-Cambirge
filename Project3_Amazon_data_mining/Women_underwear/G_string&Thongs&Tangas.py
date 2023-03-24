# https://www.amazon.co.uk/Best-Sellers-Fashion-Womens-Bikini-Briefs/zgbs/fashion/1731383031/ref=zg_bs_pg_1?_encoding=UTF8&pg=1

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

time.sleep(5)

page = 1
while page != 2:
    amazon_url = f"https://www.amazon.co.uk/Best-Sellers-Fashion-Womens-G-Strings-Thongs-Tangas/zgbs/fashion/1731384031/ref=zg_bs_pg_1?_encoding=UTF8&pg={page}"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Cookie': 'lc-acbuk=en_GB; ubid-acbuk=259-9008059-9738819; av-timezone=Europe/London; x-acbuk="oUEbWNOzMvqwgXBHYf?tj3u3E6ukokD3iuQGeUE81ZuYxmCc7@opHHLn7LjAiObz"; at-acbuk=Atza|IwEBIIXB9HHDwza7XQCvjs0VN29VOO6c4Pf6x9K5dNs7fr5M-KhAtpGHndfdDZDkcdqguGzsMbibDNaiccbKzxPh5U2xfQRFTol6pmvu2Ygwu6IQpKKju_2EPyV-gYmB5xdciRG1j2wgsxLLNd6biK4CHc_M3aNFU7E_zFfSqzV5_LoiKXypmyRPhWLoxeTaY6H176pHQnME8gQd9xthkpGWAsR8; sess-at-acbuk="zesJ6Hm24Ae6Py66wEfhIvOciZ0zLwNwuKSu2HCqn2I="; sst-acbuk=Sst1|PQH1t7k74vhS4omyTIEfZXa4Cbz1L7-mVSU1sIWTvqyVoKX0JnLGfFBoLIMaM7jaCDD7oBbHFapgYZDIPZ8dZvMGdvA96ipAVYkhhLPRl1Kl2MK4GFX3Z-C3aIC6st44YuBKUCgSl9FnvDkvTGloriIKNwGQZoUfRfOrdc76EbjWNzih3Af-j4F4H8LOtPpau8UkVP6pmaIJva22DMoKBHqw8DRxKq3y_4TEXAoLfTogXYoYxyz6_kzgX8Ey6f8OVAjYh8sd6b-D6w9qAfM2OtQRib8haBJPR03kx9l-eWCHl-8; i18n-prefs=GBP; session-id=261-0208635-7117712; session-id-time=2082787201l; session-token=uUq+OmLViz4ucSvsAnNgJslWgr8s6r2xI5nbTfDvo1juYjz6gWr9YWmtykxIUcIpt0ybDtg+mBdHN+59umTka6WE3VlgZTUaSdaO58k9ePt2RGwZX1KGvnkgzvY3MqiP8Tblh+x8k7skKS+cMnwlrPny0iWpvrwNqOZ2x77is92+kwZOr08iyShqeavK09wSqrLlBi8HnvgE7BIDOagvaofDDB3fn+Pb7ePnOew9vxYieyuBjQxFo7YowS/xgUil',
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



    web = requests.get(amazon_url,headers=headers)
    soup = BeautifulSoup(web.content, 'html.parser')

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

    Review_number.pop()
    Review_number.pop()

    print(len(Name))
    print(len(Review_score))
    print(len(Review_number))
    print(len(Price))
    print(len(Rank))

    page = int(page) + 1

data=pd.DataFrame({'Name':Name,'Review_score':Review_score,'Review_number':Review_number, 'Rank':Rank})

print(data)

MenOverall_csv_data = data.to_csv('Women_G_string&Thongs%Tangas.csv', index = True)
print(MenOverall_csv_data)

