portfolio = {}
def add_stock():
    print("ADD STOCK")

    symbol = input("Enter stock symbol (e.g. AAPL): ").strip().upper()

    if not symbol:
        print("Error: Stock symbol cannot be empty.")
        return

    try:
        shares = int(input("Enter number of shares: "))
        price = float(input("Enter purchase price per share: "))

        if shares <= 0 or price <= 0:
            print("Error: Shares and price must be greater than zero.")
            return

    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if symbol in portfolio:
        portfolio[symbol]["shares"] += shares
        portfolio[symbol]["total_cost"] += shares * price
        print(f"{symbol} updated successfully!")
    else:
        portfolio[symbol] = {
            "shares": shares,
            "total_cost": shares * price
        }
        print(f"{symbol} added successfully!")


def view_portfolio():
    print("MY STOCK PORTFOLIO")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_value = 0

    for symbol, details in portfolio.items():
        shares = details["shares"]
        cost = details["total_cost"]
        average_price = cost / shares

        print(f"Stock Symbol: {symbol}")
        print(f"Shares: {shares}")
        print(f"Average Purchase Price: ${average_price:.2f}")
        print(f"Total Purchase Value: ${cost:.2f}")

        total_value += cost

    
    print(f"Total Portfolio Value: ${total_value:.2f}")
    


def main():
    while True:
        print("STOCK PORTFOLIO TRACKER")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            print("Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()