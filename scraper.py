import requests
from bs4 import BeautifulSoup


url = "https://housing.com/in/buy/search?f=eyJsb2N0IjoicG9seSIsInBvbHkiOnsiaWQiOiJhMjczYzRjM2JlMGVlOGIzNjY5ZiJ9LCJhcGFydG1lbnRfdHlwZXMiOltdLCJwcm9wZXJ0eV9saXN0IjpbXSwicHJvcGVydHlfdHlwZXMiOltdLCJvd25lcl90eXBlcyI6W10sIm1pbl9idWRnZXRfcHJpY2UiOjAsIm1heF9idWRnZXRfcHJpY2UiOjAsImFnZSI6bnVsbCwicG9zc2Vzc2lvbiI6bnVsbCwiYmF0aHJvb21fY291bnQiOm51bGwsImhhc19nYXNfcGlwZWxpbmUiOmZhbHNlLCJoYXNfZ3ltIjpmYWxzZSwiaGFzX3N3aW1taW5nX3Bvb2wiOmZhbHNlLCJoYXNfbGlmdCI6ZmFsc2UsImhhc19wYXJraW5nIjpmYWxzZSwic2hvd19hZ2dyZWdhdGlvbnMiOnRydWUsInBhZ2VfbnVtIjoxfQ%3D%3D"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

price_raw = soup.find_all("div", {"class":"list-price"})

with open('data.txt', 'w') as f:
    str_parsed = str(price_raw)
    f.write(str_parsed)
    f.close()

with open('data.txt' , 'r') as f:
    soup3 = BeautifulSoup(f, "html.parser")
    soup3.span.unwrap()
    soup3 = soup.find_all("span", {"class": "emi-lower-value-text"})
    with open('avg.txt' , 'w') as a:
        str3 = str(soup3)
        a.write(str3)

