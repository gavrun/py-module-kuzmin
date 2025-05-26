import csv


def read_markets_csv(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def search_by_city_state(data, city, state):
    return [market for market in data 
            if market['city'].lower() == city.lower() and market['State'].lower() == state.lower()]


def search_by_zip(data, zip_code):
    return [market for market in data if market['zip'] == zip_code]


def get_market(data, market_id):
    for market in data:
        if market['FMID'] == market_id:
            return market
    return None


def sort_markets(data, key, reverse=False):
    return sorted(data, key=lambda x: x.get(key, ''), reverse=reverse)

