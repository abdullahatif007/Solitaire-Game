import tkinter as tk
import random

# Simplified game logic for demonstration
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Stock:
    def __init__(self):
        self.cards = self.initialize_deck()
        random.shuffle(self.cards)  # Shuffle for randomness

    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [Card(suit, value) for suit in suits for value in values]

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class SolitaireGUI:
    def __init__(self, master):
        self.master = master
        master.title("Klondike Solitaire")

        # Make the window size dynamic
        master.geometry("800x600")
        master.resizable(True, True)

        # Canvas setup with a different color
        self.canvas = tk.Canvas(master, bg="lightblue")
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Makes the canvas resize with the window

        # Button to start the game
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Additional button to draw a card
        self.draw_button = tk.Button(master, text="Draw Card", command=self.draw_card)
        self.draw_button.pack(side=tk.LEFT, padx=5)

        # Button to shuffle the deck
        self.shuffle_button = tk.Button(master, text="Shuffle Deck", command=self.shuffle_deck)
        self.shuffle_button.pack(side=tk.LEFT, padx=5)

        # Label to show game messages
        self.message_label = tk.Label(master, text="Welcome to Solitaire", font=("Helvetica", 12))
        self.message_label.pack()

        # Initialize stock of cards
        self.stock = Stock()

    def start_game(self):
        print("Start game button pressed.")  # Debug print
        self.message_label.config(text="Game started!")
        self.draw_initial_cards()

    def draw_initial_cards(self):
        print("Drawing initial cards...")  # Debug print
        self.canvas.delete("all")  # Clear the canvas

        x, y = 50, 100
        card_width = 70
        card_height = 100
        spacing = 120  # Increased spacing between cards

        # Draw top 5 cards
        for i in range(min(5, len(self.stock.cards))):
            card = self.stock.cards[i]
            print(f"Drawing card: {card}")  # Debug print for each card

            # Draw card rectangle with white background
            self.canvas.create_rectangle(x + i * spacing, y,
                                         x + i * spacing + card_width,
                                         y + card_height,
                                         fill="white", outline="black")

            # Center card text within the rectangle
            self.canvas.create_text(x + i * spacing + card_width // 2,
                                    y + card_height // 2,
                                    text=str(card),
                                    fill="black", font=("Helvetica", 12), width=card_width - 10)

    def draw_card(self):
        print("Drawing a card...")  # Debug print
        card = self.stock.draw_card()
        if card:
            self.message_label.config(text=f"Drew: {card}")
            self.draw_initial_cards()  # Redraw to show changes
        else:
            self.message_label.config(text="No more cards to draw!")

    def shuffle_deck(self):
        print("Shuffling the deck...")  # Debug print
        self.stock = Stock()  # Reinitialize and shuffle the deck
        self.message_label.config(text="Deck shuffled!")
        self.draw_initial_cards()

if __name__ == "__main__":
    root = tk.Tk()
    gui = SolitaireGUI(root)
    root.mainloop()
