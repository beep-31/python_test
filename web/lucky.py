import requests, webbrowser
import sys
import bs4 as bs

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.165'
GOOGLE_URL = 'https://www.google.com/search?q='
if len(sys.argv) > 1:
	for i in range(1, len(sys.argv)-1):
		sys.argv[i] = sys.argv[i] + '+'
	print('Googling...')
	link = GOOGLE_URL + ''.join(sys.argv[1:])
	headers = {"user-agent": USER_AGENT}
	res = requests.get(link, headers = headers)
	if res.status_code == 200:
		soup = bs.BeautifulSoup(res.content, 'html.parser')
		results = []
		for g in soup.find_all('div', class_='r'):
			anchors = g.find_all('a')
			if anchors:
				link = anchors[0]['href']
				title = g.find('h3').text
				item = {
					'title': title,
					'link': link
				}
				results.append(item)
		for i in range(0,5):
			webbrowser.open(results[i]['link'])
else:
	print("Write something you are looking for >>")

