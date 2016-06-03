from bs4 import BeautifulSoup
import re

with open('avg.txt' , 'r') as avg:
    soup3 = BeautifulSoup(avg, "html.parser")
    strings = str(soup3)
    price_list = int, re.findall(r'\d+', strings)
    results = int(price_list)
    print(results)

