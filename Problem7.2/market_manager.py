import csv
from market import Market

class MarketManager:
    def __init__(self, filename):
        self.filename = filename
        self.markets = self.load_markets()

    def load_markets(self):
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [Market(row) for row in reader]

    def search_by_city_state(self, city, state):
        return [m for m in self.markets if m.matches_city_state(city, state)]

    def search_by_zip(self, zip_code):
        return [m for m in self.markets if m.matches_zip(zip_code)]

    def get_market(self, market_id):
        for m in self.markets:
            if m.get_id() == market_id:
                return m
        return None

    def sort_markets(self, key, reverse=False):
        return sorted(self.markets, key=lambda m: m.get_field(key), reverse=reverse)
    
    