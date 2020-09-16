from bs4 import BeautifulSoup
import time
import requests
import os
import json

def getAmazoneprice():
    URL = 'https://www.amazon.com/Ring-Fit-Adventure-Nintendo-Switch/dp/B07XV4NHHN/ref=sr_1_1?crid=2Z177OT3SE3LT&dchild=1&keywords=ring+fit+adventure&qid=1591843734&s=videogames&sprefix=ring+%2Cvideogames%2C144&sr=1-1'
    Headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.amazon.com/Ring-Fit-Adventure-Nintendo-Switch/dp/B07XV4NHHN/ref=sr_1_1?crid=2Z177OT3SE3LT&dchild=1&keywords=ring+fit+adventure&qid=1591843734&s=videogames&sprefix=ring+%2Cvideogames%2C144&sr=1-1',
    'accept-language': 'en-US,en;q=0.9'
}
    page = requests.get(URL, headers=Headers)
    soup = BeautifulSoup(page.content, "lxml")
    availability = soup.find(id = "availability").get_text().strip()
    print(availability)

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

def getbestbuy():
    URL = 'https://www.bestbuy.com/api/tcfb/model.json?paths=%5B%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6352149%2C%22descriptions%22%2C%5B%22long%22%2C%22shortSynopsis%22%5D%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6352149%2C%22images%22%2C%220%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6352149%2C%22names%22%2C%22short%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v1%22%2C%22sites%22%2C%22skuId%22%2C6352149%2C%22sites%22%2C%22bbypres%22%2C%22relativePdpUrl%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6352149%2C%5B%22seasonDetails%22%2C%22videoDetails%22%5D%2C0%2C%22synopsis%22%5D%2C%5B%22shop%22%2C%22buttonstate%22%2C%22v5%22%2C%22item%22%2C%22skus%22%2C6352149%2C%22conditions%22%2C%22NONE%22%2C%22destinationZipCode%22%2C19148%2C%22storeId%22%2C898%2C%22context%22%2C%22cyp%22%2C%22addAll%22%2C%22false%22%5D%2C%5B%22shop%22%2C%22recommendations%22%2C%22api%22%2C%22list%22%2C%22srcs%22%2C%22dotcom-l%22%2C%22skuIds%22%2C6352149%2C%22plmts%22%2C%22cyp%22%2C%22pageSizes%22%2C10%2C%22apiKeys%22%2C%22D50%22%2C%22cyp%22%2C%22ep%22%5D%2C%5B%22shop%22%2C%22recommendations%22%2C%22api%22%2C%22list%22%2C%22srcs%22%2C%22dotcom-l%22%2C%22skuIds%22%2C6352149%2C%22plmts%22%2C%22cyp%22%2C%22pageSizes%22%2C10%2C%22apiKeys%22%2C%22D50%22%2C%22cyp%22%2C%22_entries%22%2C%7B%22from%22%3A0%2C%22to%22%3A9%7D%2C%5B%22ep%22%2C%22id%22%2C%22rank%22%5D%5D%5D&method=get'

    headers = {
        'authority': 'www.bestbuy.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.bestbuy.com/site/ring-fit-adventure-nintendo-switch/6352149.p?skuId=6352149',
        'accept-language': 'en-US,en;q=0.9'
    }
    response = requests.get(URL, headers=headers)
    response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))
    state = \
        response_formatted['jsonGraph']['shop']['buttonstate']['v5']['item']['skus']['6352149']['conditions']['NONE'][
            'destinationZipCode']['19148']['storeId']['898']['context']['cyp']['addAll']['false']['value'][
            'buttonStateResponseInfos'][0]['buttonState']
    return(state)


def main():
    #getAmazoneprice()
    #test2 = 'https://www.amazon.com/dp/B07ZNSGCNG/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07ZNSGCNG&pd_rd_w=WsGEz&pf_rd_p=48d372c1-f7e1-4b8b-9d02-4bd86f5158c5&pd_rd_wg=KtWzd&pf_rd_r=905NY56ZJS290WKKRVZ1&pd_rd_r=b9cc4716-8626-4a1d-bed6-fc65b88e09ca&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNlpXR0k2VURCNzdLJmVuY3J5cHRlZElkPUEwMDQzNjM4Mk1WMTcwWlNNVTFaTyZlbmNyeXB0ZWRBZElkPUEwOTY5MjY5WUoySkUwNUpTSElKJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    #test = 'https://www.amazon.com/Unionup-Nintendo-Switch-Adventure-Compatible-Accessories/dp/B088K6HZTZ/ref=sr_1_5?crid=2OE91OI5V98JC&dchild=1&keywords=ring+fit+adventure&qid=1591843777&s=videogames&sprefix=ring%2Cvideogames%2C147&sr=1-5'
    ringfit = 'https://www.amazon.com/Ring-Fit-Adventure-Nintendo-Switch/dp/B07XV4NHHN/ref=sr_1_1?crid=2Z177OT3SE3LT&dchild=1&keywords=ring+fit+adventure&qid=1591843734&s=videogames&sprefix=ring+%2Cvideogames%2C144&sr=1-1'
    attemps = 0
    falsereport = 0
    while(True):
        ava = getamzone(ringfit)
        state = getbestbuy()
        attemps = attemps + 1
        if (ava =='Available from these sellers.' and state =='SOLD_OUT'):
            print("Attemps: ", attemps, " ", "False Report: ", falsereport)
            print("Amazon Info: ", ava, " ", "Bestbuy Info: ", state)
        else:
            if (ava != 'Available from these sellers.'):
                print(ava)
                os.system('say "Amazon back in stock"')
            elif (state != 'SOLD_OUT'):
                print("Best buy test begin ... ")
                soldout = 0
                instock = 0
                for i in range(10):
                    state = getbestbuy()
                    if state == 'SOLD_OUT':
                        soldout = soldout + 1
                    else:
                        instock = instock + 1
                print("In stock times: ", instock)
                if instock > 5:
                    os.system('say "Best Buy back in stock"')
                else:
                    falsereport = falsereport + 1
            else:
                print(ava)
                print(state)
                os.system('say "Both Website back in stock"')
        time.sleep(5)
if __name__ == "__main__":
    main()