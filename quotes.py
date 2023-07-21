import requests
import tkinter as tk
from tkinter import messagebox

def fetch_quote():
    # Make an API request to fetch the quote data
    response = requests.get("https://stoic-quotes.com/api/quote")
    if response.status_code == 200:
        data = response.json()
        quote = data["text"]
        author = data["author"]

        # Create the main GUI window
        root = tk.Tk()
        root.title("Stoic Quote")
        root.geometry("600x400")  # Set the window size

        # Calculate the window position for centering on the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 600
        window_height = 400
        x_offset = (screen_width - window_width) // 2
        y_offset = (screen_height - window_height) // 2
        root.geometry(f"+{x_offset}+{y_offset}")

        # Create labels to display the quote and author
        quote_label = tk.Label(root, text=f'"{quote}"', font=("Helvetica", 14), wraplength=550, justify="center")
        quote_label.pack(pady=(100, 0))

        author_label = tk.Label(root, text=f"- {author}", font=("Helvetica", 12))
        author_label.pack(pady=(10, 0))

        # Add a button to close the window
        close_button = tk.Button(root, text="Close", command=root.destroy, font=("Helvetica", 12))
        close_button.pack(pady=20)

        # Run the main event loop
        root.mainloop()

    else:
        # If there was an error in the API request, show an error message
        messagebox.showerror("Error", "Failed to fetch quote. Please try again later.")

if __name__ == "__main__":
    fetch_quote()
