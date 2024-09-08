import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = 'https://example.com/search?q=Cyphers'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = []
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h2').text
        date = article.find('time').text
        source = article.find('a')['href']
        data.append({"title": title, "date": date, "source": source})

    return data
