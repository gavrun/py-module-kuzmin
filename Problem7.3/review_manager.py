import sqlite3
import os
from review import Review

class ReviewManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    # def load_reviews(self):
    #     if not os.path.exists(self.filename):
    #         return []
    #     with open(self.filename, newline='', encoding='utf-8') as f:
    #         reader = csv.DictReader(f)
    #         return [Review(row) for row in reader]

    def save_review(self, review):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO reviews (market_id, name, surname, rating, review)
            VALUES (?, ?, ?, ?, ?);
        """, (
            review.data['market_id'],
            review.data['name'],
            review.data['surname'],
            int(review.data['rating']),
            review.data['review']
        ))
        self.conn.commit()

    def get_reviews(self, market_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM reviews WHERE market_id = ?;", (market_id,))
        return [Review(dict(row)) for row in cursor.fetchall()]
    
    