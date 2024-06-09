from flask import Flask, jsonify, request
from news_aggregator import NewsAggregator
from news_filter import NewsFilter

app = Flask(__name__)

sources = [
    {'name': 'Source 1', 'url': 'http://source1.com/rss', 'category': 'beginner'},
    {'name': 'Source 2', 'url': 'http://source2.com/rss', 'category': 'expert'}
]
aggregator = NewsAggregator(sources)

@app.route('/api/news')
def get_news():
    level = request.args.get('level', 'beginner')
    articles = aggregator.fetch_news()
    filter_criteria = FilterCriteria(investor_level=level)
    news_filter = NewsFilter(articles)
    filtered_articles = news_filter.filter_by_investor_level(level)
    return jsonify([article.__dict__ for article in filtered_articles])

if __name__ == '__main__':
    app.run(debug=True)