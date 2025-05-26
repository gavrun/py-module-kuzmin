# market.py

class Market:
    def __init__(self, data):
        self.data = data

    def get_id(self):
        return self.data.get("FMID")

    def get_field(self, field):
        return self.data.get(field, '')

    def matches_city_state(self, city, state):
        return self.data.get("city", '').lower() == city.lower() and self.data.get("State", '').lower() == state.lower()

    def matches_zip(self, zip_code):
        return self.data.get("zip") == zip_code

    def display_summary(self):
        print(f"{self.data['FMID']}: {self.data['MarketName']} ({self.data['city']}, {self.data['State']})")

    def display_details(self):
        print(f"\nMarket ID: {self.data['FMID']}")
        print(f"Name: {self.data['MarketName']}")
        print(f"Address: {self.data['street']}, {self.data['city']}, {self.data['State']} {self.data['zip']}")
        print(f"Coordinates: ({self.data['y']}, {self.data['x']})")
        print(f"Website: {self.data['Website']}")
        print(f"Facebook: {self.data['Facebook']}")
        print(f"Twitter: {self.data['Twitter']}")
        print(f"Youtube: {self.data['Youtube']}")
        print(f"Other Media: {self.data['OtherMedia']}")
        print("Products:")
        for key in ['Organic', 'Bakedgoods', 'Cheese', 'Crafts', 'Flowers', 'Eggs', 'Seafood',
                    'Herbs', 'Vegetables', 'Honey', 'Jams', 'Maple', 'Meat', 'Nursery', 'Nuts',
                    'Plants', 'Poultry', 'Prepared', 'Soap', 'Trees', 'Wine', 'Coffee', 'Beans',
                    'Fruits', 'Grains', 'Juices', 'Mushrooms', 'PetFood', 'Tofu', 'WildHarvested']:
            if self.data.get(key, '').strip().upper() == 'Y':
                print(f"  - {key}")
        print("Payment Options:")
        for key in ['Credit', 'WIC', 'WICcash', 'SFMNP', 'SNAP']:
            if self.data.get(key, '').strip().upper() == 'Y':
                print(f"  - {key}")
        print(f"Last Updated: {self.data['updateTime']}")

