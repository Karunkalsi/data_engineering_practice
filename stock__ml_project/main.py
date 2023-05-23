from data_input import input_data
import pandas as pd

def run():
    # Choose which index to get the data from
    # dow, s&p, or nasdaq
    index = 'dow'

    # Choose how many tickers to compare
    number_of_tickers = 5

    best, worst = input_data(number_of_tickers=number_of_tickers, index=index)
    print_tickers(best, worst, number_of_tickers)


def print_tickers(best, worst, number_of_tickers=10):
    # Print the ticker symbols and daily percentage changes of the top 10 best performing stocks
    print(f"Top {number_of_tickers} Best Performing Stocks:")
    for stock in best:
        print(f"Ticker: {stock[0]}, Daily Pct Change: {stock[1]}")

    # Print the ticker symbols and daily percentage changes of the top 10 worst performing stocks
    print(f"\nTop {number_of_tickers} Worst Performing Stocks:")
    for stock in worst:
        print(f"Ticker: {stock[0]}, Daily Pct Change: {stock[1]}")


if __name__ == "__main__":
    run()
