import os
from market_manager import MarketManager
from review_manager import ReviewManager
from review import Review

class App:
    def __init__(self, data_file, review_file):
        self.market_manager = MarketManager(data_file)
        self.review_manager = ReviewManager(review_file)

    def run(self):
        print("Welcome to the Farmers Markets application!")
        print("Type 'help' to see available commands.\n")

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
                for market in self.market_manager.markets:
                    market.display_summary()
                print(f"\nTotal markets: {len(self.market_manager.markets)}\n")

            elif command == 'search':
                search_type = input("Search by (1) City and State or (2) ZIP code? Enter 1 or 2: ").strip()
                if search_type == '1':
                    city = input("Enter city: ").strip()
                    state = input("Enter state: ").strip()
                    results = self.market_manager.search_by_city_state(city, state)
                elif search_type == '2':
                    zip_code = input("Enter ZIP code: ").strip()
                    results = self.market_manager.search_by_zip(zip_code)
                else:
                    print("Invalid selection.")
                    continue

                if results:
                    for m in results:
                        m.display_summary()
                    print(f"\nFound {len(results)} market(s).\n")
                else:
                    print("No markets found matching the criteria.\n")

            elif command == 'details':
                market_id = input("Enter Market ID: ").strip()
                market = self.market_manager.get_market(market_id)
                if market:
                    market.display_details()
                    reviews = self.review_manager.get_reviews(market_id)
                    if reviews:
                        print("\nReviews:")
                        for r in reviews:
                            r.display()
                    else:
                        print("No reviews available for this market.\n")
                else:
                    print("Market not found.\n")

            elif command == 'review':
                market_id = input("Enter Market ID: ").strip()
                market = self.market_manager.get_market(market_id)
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
                review = Review({
                    'market_id': market_id,
                    'name': name,
                    'surname': surname,
                    'rating': rating,
                    'review': review_text
                })
                self.review_manager.save_review(review)
                print("Review added.\n")

            elif command == 'sort':
                field = input("Enter field to sort by (e.g., MarketName, city, State): ").strip()
                reverse_input = input("Sort in descending order? (y/n): ").strip().lower()
                reverse = reverse_input == 'y'
                try:
                    sorted_markets = self.market_manager.sort_markets(field, reverse)
                    for m in sorted_markets:
                        m.display_summary()
                    print()
                except KeyError:
                    print("Invalid field name.\n")

            else:
                print("Unknown command. Type 'help' to see available commands.\n")

# app main
if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'farmersmarkets', 'Export.csv')
    reviews_path = os.path.join(base_dir, 'reviews.csv')
    App(data_path, reviews_path).run()

