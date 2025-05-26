import tkinter as tk
from tkinter import ttk, messagebox
import os
from market_manager import MarketManager
from review_manager import ReviewManager
from review import Review
from gui_reviews import ReviewPanel


class MarketApp:
    def __init__(self, root, db_path):
        self.root = root
        self.root.title("Farmers Markets")

        self.market_manager = MarketManager(db_path)
        self.review_manager = ReviewManager(db_path)
        self.markets = self.market_manager.load_markets()

        # UI layout
        self.create_widgets()
        self.populate_market_list(self.markets)
        
        # UI reviews panel
        self.review_panel = ReviewPanel(self.root, self.review_manager)

    def create_widgets(self):
        # Frame for search
        search_frame = ttk.LabelFrame(self.root, text="Search by ZIP")
        search_frame.pack(fill='x', padx=10, pady=5)

        self.zip_entry = ttk.Entry(search_frame, width=20)
        self.zip_entry.pack(side='left', padx=(10, 5), pady=5)
        ttk.Button(search_frame, text="Search", command=self.search_by_zip).pack(side='left', padx=5)

        # Market list
        self.tree = ttk.Treeview(self.root, columns=("name", "city", "state"), show='headings')
        self.tree.heading("name", text="Market Name")
        self.tree.heading("city", text="City")
        self.tree.heading("state", text="State")
        self.tree.column("name", width=300)
        self.tree.pack(fill='both', expand=True, padx=10, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_market_selected)

        # Details panel
        self.details_text = tk.Text(self.root, height=15, wrap='word')
        self.details_text.pack(fill='both', expand=True, padx=10, pady=(0, 10))

    def populate_market_list(self, markets):
        self.tree.delete(*self.tree.get_children())
        for market in markets:
            self.tree.insert("", "end", iid=market.get_id(), values=(
                market.get_field("market_name"),
                market.get_field("city"),
                market.get_field("state")
            ))

    def search_by_zip(self):
        zip_code = self.zip_entry.get().strip()
        if not zip_code:
            messagebox.showwarning("Input needed", "Enter a ZIP code.")
            return
        results = self.market_manager.search_by_zip(zip_code)
        if not results:
            messagebox.showinfo("No results", f"No markets found for ZIP: {zip_code}")
        self.populate_market_list(results)

    def on_market_selected(self, event):
        selected = self.tree.focus()
        if not selected:
            return
        market = self.market_manager.get_market(selected)
        self.show_market_details(market)
        self.review_panel.set_market_id(market.get_id())

    def show_market_details(self, market):
        self.details_text.delete("1.0", tk.END)
        lines = [
            f"Market ID: {market.get_id()}",
            f"Name: {market.get_field('market_name')}",
            f"Address: {market.get_field('street')}, {market.get_field('city')}, {market.get_field('state')} {market.get_field('zip')}",
            f"Coordinates: ({market.get_field('y')}, {market.get_field('x')})",
            f"Website: {market.get_field('website')}",
            f"Facebook: {market.get_field('facebook')}",
            f"Twitter: {market.get_field('twitter')}",
            f"Youtube: {market.get_field('youtube')}",
            f"Other Media: {market.get_field('other_media')}",
            "",
            "Products:"
        ]
        for key in ['organic', 'bakedgoods', 'cheese', 'crafts', 'flowers', 'eggs', 'seafood',
                    'herbs', 'vegetables', 'honey', 'jams', 'maple', 'meat', 'nursery', 'nuts',
                    'plants', 'poultry', 'prepared', 'soap', 'trees', 'wine', 'coffee', 'beans',
                    'fruits', 'grains', 'juices', 'mushrooms', 'petfood', 'tofu', 'wildharvested']:
            if market.get_field(key).strip().upper() == 'Y':
                lines.append(f"  - {key.capitalize()}")

        lines.append("")
        lines.append("Payment Options:")
        for key in ['credit', 'wic', 'wiccash', 'sfmnp', 'snap']:
            if market.get_field(key).strip().upper() == 'Y':
                lines.append(f"  - {key.upper()}")

        lines.append(f"\nLast Updated: {market.get_field('update_time')}")

        self.details_text.insert("1.0", "\n".join(lines))

# UI entry point
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "farmersmarkets.db")

    root = tk.Tk()
    app = MarketApp(root, db_path)
    root.mainloop()

