# re-factoring later now it's to get shit working.
from re import findall, compile, search 
from requests import get
#import feedparser

urls = {'https://www.vg.no/', 'https://www.nrk.no/', 'https://www.tek.no/','https://itavisen.no/', 'http://4chan.org/g/'}
pattern = compile('((https|http)://\S+(\.rss|\=rss|/feed/|.xml))')
feedUrls = []

def getData(url): return get(url).text

def findRssfeed(url):
	source = getData(url)
	loot = search(pattern, source)

	try:
		return (loot.group())
	except AttributeError as e:
		pass

# parse rss feeds
# title
# description
# img ?
# url for article
def feedParsing(url): 
	print (url)
	#feed = feedparser.parse()


def ParseFeed():
	for url in urls:
		feedUrl = findRssfeed(url)
		if feedUrl is None:
			pass
		else:
			feedUrls.append(feedUrl)

if __name__ == '__main__':
	ParseFeed()
	for url in feedUrls:
		feedParsing(url)
