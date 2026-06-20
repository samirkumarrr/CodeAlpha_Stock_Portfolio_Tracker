import tkinter as tk
from tkinter import messagebox

# Stock Prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

# Add Stock Function
def add_stock():
    stock = stock_entry.get().upper()
    quantity = quantity_entry.get()

    if stock not in stock_prices:
        messagebox.showerror("Error", "Stock not found!")
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid quantity!")
        return

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    portfolio_list.insert(
        tk.END,
        f"{stock} - {quantity} shares"
    )

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Calculate Portfolio Value
def calculate_value():
    total = 0
    result_text.delete(1.0, tk.END)

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total += value

        result_text.insert(
            tk.END,
            f"{stock}: {quantity} × ${stock_prices[stock]} = ${value}\n"
        )

    result_text.insert(
        tk.END,
        f"\nTotal Portfolio Value = ${total}"
    )

    # Save report
    with open("portfolio_report.txt", "w") as file:
        file.write(result_text.get(1.0, tk.END))

# GUI Window
root = tk.Tk()
root.title("Stock Portfolio Tracker")
root.geometry("500x500")

title = tk.Label(
    root,
    text="Stock Portfolio Tracker",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

tk.Label(root, text="Stock Symbol").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(
    root,
    text="Add Stock",
    command=add_stock
).pack(pady=10)

portfolio_list = tk.Listbox(root, width=40)
portfolio_list.pack(pady=10)

tk.Button(
    root,
    text="Calculate Portfolio Value",
    command=calculate_value
).pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

root.mainloop()