import sqlite3
import csv
import os

FIELD_MAP = {
    # market
    'fmid': 'FMID',
    'market_name': 'MarketName',
    'street': 'street',
    'city': 'city',
    'county': 'County',
    'state': 'State',
    'zip': 'zip',
    'x': 'x',
    'y': 'y',
    'website': 'Website',
    'facebook': 'Facebook',
    'twitter': 'Twitter',
    'youtube': 'Youtube',
    'other_media': 'OtherMedia',
    'update_time': 'updateTime',
    # payment
    'credit': 'Credit', 'wic': 'WIC', 'wiccash': 'WICcash', 'sfmnp': 'SFMNP', 'snap': 'SNAP',
    # products
    'organic': 'Organic', 'bakedgoods': 'Bakedgoods', 'cheese': 'Cheese', 'crafts': 'Crafts',
    'flowers': 'Flowers', 'eggs': 'Eggs', 'seafood': 'Seafood', 'herbs': 'Herbs',
    'vegetables': 'Vegetables', 'honey': 'Honey', 'jams': 'Jams', 'maple': 'Maple',
    'meat': 'Meat', 'nursery': 'Nursery', 'nuts': 'Nuts', 'plants': 'Plants',
    'poultry': 'Poultry', 'prepared': 'Prepared', 'soap': 'Soap', 'trees': 'Trees',
    'wine': 'Wine', 'coffee': 'Coffee', 'beans': 'Beans', 'fruits': 'Fruits',
    'grains': 'Grains', 'juices': 'Juices', 'mushrooms': 'Mushrooms',
    'petfood': 'PetFood', 'tofu': 'Tofu', 'wildharvested': 'WildHarvested'
}

def create_schema(conn, schema_file):
    with open(schema_file, encoding='utf-8') as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()

def load_markets_csv(conn, csv_path):
    fields = list(FIELD_MAP.keys())
    cursor = conn.cursor()
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            values = [row.get(FIELD_MAP[field], '').strip() for field in fields]
            cursor.execute(f"""
                INSERT INTO markets ({', '.join(fields)})
                VALUES ({', '.join(['?'] * len(fields))});
            """, values)
    conn.commit()

def load_reviews_csv(conn, csv_path):
    if not os.path.exists(csv_path):
        return
    cursor = conn.cursor()
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO reviews (
                    market_id, name, surname, rating, review
                ) VALUES (?, ?, ?, ?, ?);
            """, (
                row['market_id'], row['name'], row['surname'], int(row['rating']), row['review']
            ))
    conn.commit()

if __name__ == "__main__":
    print("Initializing database...")

    base_path = os.path.dirname(__file__)
    schema_path = os.path.join(base_path, 'schema.sql')
    db_path = os.path.join(base_path, 'farmersmarkets.db')
    markets_csv = os.path.join(base_path, 'farmersmarkets', 'Export.csv')
    reviews_csv = os.path.join(base_path, 'reviews', 'reviews.csv')

    conn = sqlite3.connect(db_path)
    create_schema(conn, schema_path)
    print("Loading data...")
    load_markets_csv(conn, markets_csv)
    load_reviews_csv(conn, reviews_csv)
    conn.close()

    print("Database and data loaded initialized.")
