from bs4 import BeautifulSoup

markup = '<a class="list-price" href="http://example.com/">I linked to <i>example.com</i></a> <p class="test">123</p><a class="not-it"></a>'
soup = BeautifulSoup(markup, "html.parser")

str = soup.find_all("a", {"class": "list-price"})

soup1 = BeautifulSoup(str, "html.parser")

soup1.i.unwrap()
soup1.a.unwrap()
print(soup1)
