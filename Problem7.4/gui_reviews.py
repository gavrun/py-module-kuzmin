import tkinter as tk
from tkinter import ttk, messagebox
from review import Review


class ReviewPanel:
    def __init__(self, parent, review_manager):
        self.review_manager = review_manager

        self.frame = ttk.LabelFrame(parent, text="Reviews")
        self.frame.pack(fill='x', padx=10, pady=5)

        # Display area
        self.text = tk.Text(self.frame, height=8, wrap='word', state='disabled')
        self.text.pack(fill='both', padx=5, pady=5)

        # Add review form
        form_frame = ttk.Frame(self.frame)
        form_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(form_frame, text="Name:").grid(row=0, column=0)
        self.entry_name = ttk.Entry(form_frame, width=15)
        self.entry_name.grid(row=0, column=1)

        ttk.Label(form_frame, text="Surname:").grid(row=0, column=2)
        self.entry_surname = ttk.Entry(form_frame, width=15)
        self.entry_surname.grid(row=0, column=3)

        ttk.Label(form_frame, text="Rating (1-5):").grid(row=1, column=0)
        self.entry_rating = ttk.Entry(form_frame, width=5)
        self.entry_rating.grid(row=1, column=1)

        ttk.Label(form_frame, text="Review:").grid(row=1, column=2)
        self.entry_text = ttk.Entry(form_frame, width=30)
        self.entry_text.grid(row=1, column=3)

        self.submit_button = ttk.Button(form_frame, text="Add Review", command=self.submit_review)
        self.submit_button.grid(row=2, column=3, pady=5, sticky='e')

        self.current_market_id = None

    def display_reviews(self, reviews):
        self.text.configure(state='normal')
        self.text.delete("1.0", tk.END)
        if not reviews:
            self.text.insert(tk.END, "No reviews for this market.")
        else:
            for review in reviews:
                self.text.insert(tk.END, f"{review.data['name']} {review.data['surname']} ({review.data['rating']}):\n")
                self.text.insert(tk.END, f"{review.data['review']}\n\n")
        self.text.configure(state='disabled')

    def set_market_id(self, market_id):
        self.current_market_id = market_id
        self.refresh()

    def refresh(self):
        if self.current_market_id:
            reviews = self.review_manager.get_reviews(self.current_market_id)
            self.display_reviews(reviews)

    def submit_review(self):
        if not self.current_market_id:
            return
        name = self.entry_name.get().strip()
        surname = self.entry_surname.get().strip()
        rating = self.entry_rating.get().strip()
        text = self.entry_text.get().strip()

        if not name or not surname or not rating or not text:
            messagebox.showwarning("Incomplete", "Please fill in all review fields.")
            return

        try:
            rating = int(rating)
            if not (1 <= rating <= 5):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid rating", "Rating must be an integer from 1 to 5.")
            return

        review = Review({
            'market_id': self.current_market_id,
            'name': name,
            'surname': surname,
            'rating': rating,
            'review': text
        })

        self.review_manager.save_review(review)
        self.refresh()

        # Clear form
        self.entry_name.delete(0, tk.END)
        self.entry_surname.delete(0, tk.END)
        self.entry_rating.delete(0, tk.END)
        self.entry_text.delete(0, tk.END)

