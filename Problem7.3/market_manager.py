import sqlite3
from market import Market

class MarketManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def load_markets(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM markets;")
        return [Market(dict(row)) for row in cursor.fetchall()]

    def search_by_city_state(self, city, state):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM markets WHERE lower(city) = ? AND lower(state) = ?;
        """, (city.lower(), state.lower()))
        return [Market(dict(row)) for row in cursor.fetchall()]

    def search_by_zip(self, zip_code):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM markets WHERE zip = ?;", (zip_code,))
        return [Market(dict(row)) for row in cursor.fetchall()]

    def get_market(self, market_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM markets WHERE fmid = ?;", (market_id,))
        row = cursor.fetchone()
        return Market(dict(row)) if row else None

    def sort_markets(self, key, reverse=False):
        direction = "DESC" if reverse else "ASC"
        
        cursor = self.conn.cursor()
        query = f"SELECT * FROM markets ORDER BY {key} COLLATE NOCASE {direction};"
        try:
            cursor.execute(query)
            return [Market(dict(row)) for row in cursor.fetchall()]
        except sqlite3.OperationalError:
            raise KeyError(f"Field '{key}' does not exist in table.")
        

