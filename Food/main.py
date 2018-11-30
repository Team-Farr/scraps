import requests, base64

def getData(url):
    noPromo={'app-promo':'yes'}
    return requests.get(url, cookies=noPromo).json()


def foodCategory(cat="godis"):
    offer = getData((base64.b64decode('aHR0cHM6Ly9hcGkubWF0dGlsYnVkLmNvbS92MS9vZmZlcnMvYXVzdGFnZGVyL2NhdGVnb3JpZXM=').decode('utf-8')))

    for element in offer['categories']:
        title = element['itemsUrl'].split('/')[-2]
        if cat in title:
            return (element['itemsUrl'])



print (foodCategory())

