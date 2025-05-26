import csv
import os


# REVIEW_FILE = 'reviews.csv'


def load_reviews(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_review(filename, review):
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['market_id', 'name', 'surname', 'rating', 'review']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(review)


def get_reviews(reviews, market_id):
    return [review for review in reviews if review['market_id'] == market_id]

