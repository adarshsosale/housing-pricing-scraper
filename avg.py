from bs4 import BeautifulSoup

with open('avg.txt' , 'r') as avg:
    soup3 = BeautifulSoup(avg, "html.parser")
    for span in soup3:
        soup3.span.unwrap()
        print(soup3)

def parseIntegers(mixedList):
    return [x for x in testList if (isinstance(x, int) or isinstance(x, long)) and not isinstance(x, bool)]