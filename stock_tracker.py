
stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "MICROSOFT": 420,
    "AMAZON": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:")

for stock in stock_prices:
    print(stock, "-", "$", stock_prices[stock])

print()

number_of_stocks = int(input("How many different stocks do you want to add? "))

for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock_name] = quantity


print("\n===== Portfolio =====")
total_investment = 0

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    value = price * quantity

    total_investment += value

    print(stock,"| Quantity:", quantity,"| Price: $", price,"| Value: $", value)

print("\nTotal Investment: $", total_investment)

with open("portfolio.txt", "w") as file:

    file.write("Stock Portfolio Report\n")
    file.write("======================\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        file.write(f"{stock} | Quantity: {quantity} | "f"Price: ${price} | Value: ${value}\n")

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved to portfolio.txt")