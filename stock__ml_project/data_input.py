import yfinance as yf
import yahoo_fin.stock_info as si
import pandas as pd


def input_data(number_of_tickers: int, index: str):
    """
    This function takes in a select number of tickers and returns a dataframe
    with that amount of top producers
    :param number_of_tickers: int of top producers
    :return: top and worst producers: dataframe
    """
    index_dict = {
        "dow": si.tickers_dow(),
        "s&p": si.tickers_sp500(),
        "nasdaq": si.tickers_nasdaq()
    }

    all_producers = index_dict[index]

    # Create an empty dictionary to store the daily percentage changes of the companies
    daily_pct_change_dict = {}

    # Iterate over the companies and retrieve their daily percentage change
    for company in all_producers:
        try:
            data = si.get_data(company)
            data['Daily_Pct_Change'] = data['close'].pct_change() * 100
            daily_pct_change = data['Daily_Pct_Change'].iloc[-1]
            daily_pct_change_dict[company] = daily_pct_change
        except KeyError:
            continue

    # Sort the daily percentage changes in descending order
    sorted_pct_changes = sorted(daily_pct_change_dict.items(), key=lambda x: x[1], reverse=True)

    # Get the top 10 best performing stocks
    top_10_best = sorted_pct_changes[:number_of_tickers]

    # Get the top 10 worst performing stocks
    top_10_worst = sorted_pct_changes[-number_of_tickers:]

    return top_10_best, top_10_worst


if __name__ == "__main__":
    print(input_data(10))
