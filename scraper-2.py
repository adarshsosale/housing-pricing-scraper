from lxml import html
import requests

url = "https://housing.com/in/buy/search?f=eyJsb2N0IjoicG9seSIsInBvbHkiOnsiaWQiOiJhMjczYzRjM2JlMGVlOGIzNjY5ZiJ9LCJhcGFydG1lbnRfdHlwZXMiOltdLCJwcm9wZXJ0eV9saXN0IjpbXSwicHJvcGVydHlfdHlwZXMiOltdLCJvd25lcl90eXBlcyI6W10sIm1pbl9idWRnZXRfcHJpY2UiOjAsIm1heF9idWRnZXRfcHJpY2UiOjAsImFnZSI6bnVsbCwicG9zc2Vzc2lvbiI6bnVsbCwiYmF0aHJvb21fY291bnQiOm51bGwsImhhc19nYXNfcGlwZWxpbmUiOmZhbHNlLCJoYXNfZ3ltIjpmYWxzZSwiaGFzX3N3aW1taW5nX3Bvb2wiOmZhbHNlLCJoYXNfbGlmdCI6ZmFsc2UsImhhc19wYXJraW5nIjpmYWxzZSwic2hvd19hZ2dyZWdhdGlvbnMiOnRydWUsInBhZ2VfbnVtIjoxfQ%3D%3D"

page = requests.get(url)
tree = html.fromstring(page.text) # corrected, used to be `lxml.html.fromstring`

attr = "//@data-price"
price = tree.xpath(attr)

print (price)