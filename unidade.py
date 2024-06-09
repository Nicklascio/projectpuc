import unittest
from news_aggregator import NewsAggregator, NewsArticle
from news_filter import NewsFilter

class TestNewsAggregator(unittest.TestCase):
    def setUp(self):
        self.sources = [
            {'name': 'Source 1', 'url': 'http://source1.com/rss', 'category': 'beginner'},
            {'name': 'Source 2', 'url': 'http://source2.com/rss', 'category': 'expert'}
        ]
        self.aggregator = NewsAggregator(self.sources)

    def test_fetch_news(self):
        articles = self.aggregator.fetch_news()
        self.assertGreater(len(articles), 0)
        for article in articles:
            self.assertIsInstance(article, NewsArticle)

class TestNewsFilter(unittest.TestCase):
    def setUp(self):
        self.articles = [
            NewsArticle('Title 1', 'Source 1', '2024-01-01', 'Content 1', 'http://example.com/1', 'beginner'),
            NewsArticle('Title 2', 'Source 2', '2024-01-02', 'Content 2', 'http://example.com/2', 'expert')
        ]
        self.filter = NewsFilter(self.articles)

    def test_filter_by_investor_level(self):
        beginner_articles = self.filter.filter_by_investor_level('beginner')
        self.assertEqual(len(beginner_articles), 1)
        self.assertEqual(beginner_articles[0].title, 'Title 1')

        expert_articles = self.filter.filter_by_investor_level('expert')
        self.assertEqual(len(expert_articles), 1)
        self.assertEqual(expert_articles[0].title, 'Title 2')

if __name__ == '__main__':
    unittest.main()