class FilterCriteria:
    def __init__(self, investor_level=None):
        self.investor_level = investor_level

class NewsFilter:
    def __init__(self, articles):
        self.articles = articles

    def filter_by_investor_level(self, investor_level):
        return [article for article in self.articles if article.category == investor_level]