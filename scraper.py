import json
import requests
from bs4 import BeautifulSoup


url = "https://housing.com/in/buy/search?f=eyJsb2N0IjoicG9seSIsInBvbHkiOnsiaWQiOiJhMjczYzRjM2JlMGVlOGIzNjY5ZiJ9LCJhcGFydG1lbnRfdHlwZXMiOltdLCJwcm9wZXJ0eV9saXN0IjpbXSwicHJvcGVydHlfdHlwZXMiOltdLCJvd25lcl90eXBlcyI6W10sIm1pbl9idWRnZXRfcHJpY2UiOjAsIm1heF9idWRnZXRfcHJpY2UiOjAsImFnZSI6bnVsbCwicG9zc2Vzc2lvbiI6bnVsbCwiYmF0aHJvb21fY291bnQiOm51bGwsImhhc19nYXNfcGlwZWxpbmUiOmZhbHNlLCJoYXNfZ3ltIjpmYWxzZSwiaGFzX3N3aW1taW5nX3Bvb2wiOmZhbHNlLCJoYXNfbGlmdCI6ZmFsc2UsImhhc19wYXJraW5nIjpmYWxzZSwic2hvd19hZ2dyZWdhdGlvbnMiOnRydWUsInBhZ2VfbnVtIjoxfQ%3D%3D"

r = requests.get(url)
soup = BeautifulSoup(r.content)

price_raw = soup.span.string.wrap(soup.new_tag("p"))

'''price_raw = soup.find_all(attrs={"data-price": "value"}) '''

'''price_raw = soup.find_all("div", {"class":"list-price"})'''

price = str(price_raw)
print (price)

'''
    for span in soup.find_all('span'):
        with open('data.txt', 'w') as f:
            f.write(span.text)
'''