import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p> This is a test tag</p>")
new_string = soup.p.string.wrap(soup.new_tag("b"))
string =  str(new_string)
print (string)
