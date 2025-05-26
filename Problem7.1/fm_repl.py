import csv
import os

from fm_farmers import (
    read_markets_csv,
    search_by_city_state,
    search_by_zip,
    get_market,
    sort_markets
)

from fm_review import (
    load_reviews,
    save_review,
    get_reviews
)

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'farmersmarkets', 'Export.csv')

REVIEWS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reviews.csv')


def print_market_summary(market):
    print(f"{market['FMID']}: {market['MarketName']} ({market['city']}, {market['State']})")


def print_market_details(market):
    print(f"\nMarket ID: {market['FMID']}")
    print(f"Name: {market['MarketName']}")
    print(f"Address: {market['street']}, {market['city']}, {market['State']} {market['zip']}")
    print(f"Coordinates: ({market['y']}, {market['x']})")
    print(f"Website: {market['Website']}")
    print(f"Facebook: {market['Facebook']}")
    print(f"Twitter: {market['Twitter']}")
    print(f"Youtube: {market['Youtube']}")
    print(f"Other Media: {market['OtherMedia']}")
    print(f"Products:")
    for key in ['Organic', 'Bakedgoods', 'Cheese', 'Crafts', 'Flowers', 'Eggs', 'Seafood',
                'Herbs', 'Vegetables', 'Honey', 'Jams', 'Maple', 'Meat', 'Nursery', 'Nuts',
                'Plants', 'Poultry', 'Prepared', 'Soap', 'Trees', 'Wine', 'Coffee', 'Beans',
                'Fruits', 'Grains', 'Juices', 'Mushrooms', 'PetFood', 'Tofu', 'WildHarvested']:
        if market.get(key, '').strip().upper() == 'Y':
            print(f"  - {key}")
    print(f"Payment Options:")
    for key in ['Credit', 'WIC', 'WICcash', 'SFMNP', 'SNAP']:
        if market.get(key, '').strip().upper() == 'Y':
            print(f"  - {key}")
    print(f"Last Updated: {market['updateTime']}")


def print_reviews(reviews):
    if not reviews:
        print("No reviews available for this market.")
        return
    print("\nReviews:")
    for review in reviews:
        print(f"- {review['name']} {review['surname']} (Rating: {review['rating']})")
        print(f"  {review['review']}\n")


def main():
    print("Welcome to the Farmers Markets application!")
    print("Type 'help' to see available commands.\n")

    # markets = read_markets_csv(DATA_FILE)
    # reviews = load_reviews(REVIEWS_FILE)

    try:
        markets = read_markets_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: Data file '{DATA_FILE}' not found.")
        return

    try:
        reviews = load_reviews(REVIEWS_FILE)
    except Exception as e:
        print(f"Error loading reviews: {e}")
        reviews = []

    while True:
        command = input("Enter command: ").strip().lower()

        if command == 'exit':
            print("Exiting the Farmers Markets application.")
            break

        elif command == 'help':
            print("\nAvailable commands:")
            print("  list                     - List all markets")
            print("  search                   - Search markets by city/state or ZIP code")
            print("  details                  - Show details of a specific market by ID")
            print("  review                   - Add a review for a market")
            print("  sort                     - Sort markets by a specific field")
            print("  help                     - Show this help message")
            print("  exit                     - Exit the application\n")

        elif command == 'list':
            for market in markets:
                print_market_summary(market)
            print(f"\nTotal markets: {len(markets)}\n")

        elif command == 'search':
            search_type = input("Search by (1) City and State or (2) ZIP code? Enter 1 or 2: ").strip()
            if search_type == '1':
                city = input("Enter city: ").strip()
                state = input("Enter state: ").strip()
                results = search_by_city_state(markets, city, state)
            elif search_type == '2':
                zip_code = input("Enter ZIP code: ").strip()
                results = search_by_zip(markets, zip_code)
            else:
                print("Invalid selection.")
                continue

            if results:
                for market in results:
                    print_market_summary(market)
                print(f"\nFound {len(results)} market(s).\n")
            else:
                print("No markets found matching the criteria.\n")

        elif command == 'details':
            market_id = input("Enter Market ID: ").strip()
            market = get_market(markets, market_id)
            if market:
                print_market_details(market)
                market_reviews = get_reviews(reviews, market_id)
                print_reviews(market_reviews)
            else:
                print("Market not found.\n")

        elif command == 'review':
            market_id = input("Enter Market ID: ").strip()
            market = get_market(markets, market_id)
            if not market:
                print("Market not found.\n")
                continue
            name = input("Enter your first name: ").strip()
            surname = input("Enter your surname: ").strip()
            while True:
                try:
                    rating = int(input("Enter rating (1-5): ").strip())
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a valid integer.")
            review_text = input("Enter your review: ").strip()
            review_entry = {
                'market_id': market_id,
                'name': name,
                'surname': surname,
                'rating': rating,
                'review': review_text
            }
            save_review(REVIEWS_FILE, review_entry)
            reviews.append(review_entry)
            print("Review added.\n")

        elif command == 'sort':
            field = input("Enter field to sort by (e.g., MarketName, city, State): ").strip()
            reverse_input = input("Sort in descending order? (y/n): ").strip().lower()
            reverse = reverse_input == 'y'
            try:
                sorted_markets = sort_markets(markets, field, reverse)
                for market in sorted_markets:
                    print_market_summary(market)
                print()
            except KeyError:
                print("Invalid field name.\n")

        else:
            print("Unknown command. Type 'help' to see available commands.\n")

# main
if __name__ == "__main__":
    main()

