from bs4 import BeautifulSoup
import time
import requests
import os

def getamzone(url):
    URL = url
    Headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': url,
        'accept-language': 'en-US,en;q=0.9'
    }
    page = requests.get(URL, headers=Headers)
    soup = BeautifulSoup(page.content, "lxml")
    availability = soup.find(id="availability").get_text().strip()
    return(availability)

def main():
    ringfit = 'https://www.amazon.com/Ring-Fit-Adventure-Nintendo-Switch/dp/B07XV4NHHN/ref=sr_1_1?crid=2Z177OT3SE3LT&dchild=1&keywords=ring+fit+adventure&qid=1591843734&s=videogames&sprefix=ring+%2Cvideogames%2C144&sr=1-1'
    attemps = 0
    instock = 0
    while(True):
        ava = getamzone(ringfit)
        attemps = attemps + 1
        if (ava =='Available from these sellers.'):
            print("Attemps: ", attemps, " ", "In stock times: ", instock)
            print("Amazon Info: ", ava)
        else:
            instock = instock + 1
            print(ava)
            os.system('say "Amazon back in stock"')
        time.sleep(5)
if __name__ == "__main__":
    main()