import requests, base64

def getData(url):
    noPromo={'app-promo':'yes'}
    return requests.get(url, cookies=noPromo).json()

def foodCategory(cat=""):
    offer = getData((base64.b64decode('aHR0cHM6Ly9hcGkubWF0dGlsYnVkLmNvbS92MS9vZmZlcnMvYXVzdGFnZGVyL2NhdGVnb3JpZXM=').decode('utf-8')))
    avaliableID = ["husholdning", "hygiene", "kjottdeig", "kyllingfilet", "fisk", "ost", "ferdigmat", "brus", "godis", "kaffe"]

    if cat == "":
    	return ("please give me a valid id ", avaliableID)

    if cat in avaliableID:
	    for element in offer['categories']:
	        title = element['itemsUrl'].split('/')[-2]
	        if cat in title:
	            return (element['itemsUrl'])

def foodStore(cat=""): #denne funker ikke helt ordentlig enda, use with caution
    offer = getData((base64.b64decode('aHR0cHM6Ly9hcGkubWF0dGlsYnVkLmNvbS92MS9vZmZlcnMvYXVzdGFnZGVyL3N0b3Jlcw==').decode('utf-8')))
    avaliableID = ["husholdning", "hygiene", "kjottdeig", "kyllingfilet", "fisk", "ost", "ferdigmat", "brus", "godis", "kaffe"]

    if cat == "":
    	return ("please give me a valid id ", avaliableID)

    if cat in avaliableID:
	    for element in offer['categories']:
	        title = element['title'].split('/')[-2]
	        if cat in title:
	            return (element['title'])

if __name__ == '__main__':
	print (foodCategory(""))
