class Market:
    def __init__(self, data):
        self.data = {k.lower(): v for k, v in data.items()}

    def get_id(self):
        return self.data.get("fmid")

    def get_field(self, field):
        return self.data.get(field, '')

    def matches_city_state(self, city, state):
        return self.data.get("city", '').lower() == city.lower() and self.data.get("state", '').lower() == state.lower()

    def matches_zip(self, zip_code):
        return self.data.get("zip") == zip_code

    def display_summary(self):
        print(f"{self.data['fmid']}: {self.data['market_name']} ({self.data['city']}, {self.data['state']})")

    def display_details(self):
        print(f"\nMarket ID: {self.data['fmid']}")
        print(f"Name: {self.data['market_name']}")
        print(f"Address: {self.data['street']}, {self.data['city']}, {self.data['state']} {self.data['zip']}")
        print(f"Coordinates: ({self.data['y']}, {self.data['x']})")
        print(f"Website: {self.data['website']}")
        print(f"Facebook: {self.data['facebook']}")
        print(f"Twitter: {self.data['twitter']}")
        print(f"Youtube: {self.data['youtube']}")
        print(f"Other Media: {self.data['other_media']}")
        print("Products:")
        for key in ['organic', 'bakedgoods', 'cheese', 'crafts', 'flowers', 'eggs', 'seafood',
                    'herbs', 'vegetables', 'honey', 'jams', 'maple', 'meat', 'nursery', 'nuts',
                    'plants', 'poultry', 'prepared', 'soap', 'trees', 'wine', 'coffee', 'beans',
                    'fruits', 'grains', 'juices', 'mushrooms', 'petfood', 'tofu', 'wildharvested']:
            if self.data.get(key, '').strip().upper() == 'Y':
                print(f"  - {key}")
        print("Payment Options:")
        for key in ['credit', 'wic', 'wiccash', 'sfmnp', 'snap']:
            if self.data.get(key, '').strip().upper() == 'Y':
                print(f"  - {key}")
        print(f"Last Updated: {self.data['update_time']}")

