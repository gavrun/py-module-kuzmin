class Review:
    def __init__(self, data):
        self.data = data

    def get_market_id(self):
        return self.data.get("market_id")

    def display(self):
        print(f"- {self.data['name']} {self.data['surname']} (Rating: {self.data['rating']})")
        print(f"  {self.data['review']}\n")

        