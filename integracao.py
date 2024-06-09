import unittest
import requests

class TestIntegration(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/news'

    def test_get_news(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for article in data:
            self.assertIn('title', article)
            self.assertIn('content', article)
            self.assertIn('url', article)

    def test_get_news_with_level(self):
        response = requests.get(f'{self.BASE_URL}?level=beginner')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        for article in data:
            self.assertEqual(article['category'], 'beginner')

if __name__ == '__main__':
    unittest.main()