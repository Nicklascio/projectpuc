import requests
from bs4 import BeautifulSoup

class NewsArticle:
    def __init__(self, title, source, published_date, content, url, category):
        self.title = title
        self.source = source
        self.published_date = published_date
        self.content = content
        self.url = url
        self.category = category

class NewsAggregator:
    def __init__(self, sources):
        self.sources = sources

    def fetch_news(self):
        articles = []
        for source in self.sources:
            response = requests.get(source['url'])
            soup = BeautifulSoup(response.content, 'html.parser')
            for item in soup.find_all('item'):
                article = NewsArticle(
                    title=item.title.text,
                    source=source['name'],
                    published_date=item.pubDate.text,
                    content=item.description.text,
                    url=item.link.text,
                    category=source['category']
                )
                articles.append(article)
        return articles