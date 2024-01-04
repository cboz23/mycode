import yfinance as yf
import time

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'].iloc[-1]
        return price
    except Exception as e:
        print(f"Error fetching stock price for {symbol}: {e}")
        return None

def main():
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Add or remove stock symbols as needed

    print("Stock Price Updater")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            for symbol in stock_symbols:
                price = get_stock_price(symbol)
                if price is not None:
                    print(f"{symbol}: ${price:.2f}")

            print("\nWaiting for the next update...\n")
            time.sleep(60)  # Update every 60 seconds

    except KeyboardInterrupt:
        print("\nExiting Stock Price Updater.")

if __name__ == "__main__":
    main()

