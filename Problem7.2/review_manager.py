import csv
import os
from review import Review

class ReviewManager:
    def __init__(self, filename):
        self.filename = filename
        self.reviews = self.load_reviews()

    def load_reviews(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [Review(row) for row in reader]

    def save_review(self, review):
        file_exists = os.path.exists(self.filename)
        with open(self.filename, 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['market_id', 'name', 'surname', 'rating', 'review']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(review.data)
        self.reviews.append(review)

    def get_reviews(self, market_id):
        return [r for r in self.reviews if r.get_market_id() == market_id]
    
    