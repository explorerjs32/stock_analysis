import numpy as np
import pandas as pd
import os
import yfinance as yf
from datetime import date, datetime
from natsort import natsorted, index_natsorted, order_by_index

def add_shares(portfolio, portfolio_dir, portfolio_name):
    print('Modify stocks in your portfolio:\n')

    # Add the new data. You want to select the Ticker you wish to modify and select the date you purchased the new shares
    ticker = str(input('What is the stock Ticker? '))
    mod_date = str(input('What is the purchase date (YYYY-MM-DD)? '))
    mod_time = str(input('What is the purchase time (hh:mm:ss)? '))

    # Look for the indext in your portfolio where this holding is located
    index = np.where(portfolio['Ticker'] == ticker)[0][0]

    # Extract the stoc data and re-format the Datetime column
    data = yf.download(ticker, mod_date, interval='1m')
    data = data.reset_index()
    data['Datetime'] = [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in data['Datetime']]
    dt_index = np.where(data.Datetime == mod_date + ' ' + mod_time)[0][0]

    # Get the stock price and how much you purchased
    purchase = float(input('How much did you purchase? '))
    price = data.iloc[dt_index]['Close']


    # Calculate the number of shares you purchased and add them to the exixting shares
    shares = purchase/price
    portfolio.Shares[index] = round(portfolio.Shares[index] + shares, 5)

    # Modify the total amount invested
    portfolio.Amount_Invested[index] = round(portfolio.Amount_Invested[index] + purchase, 2)

    # Calcuate the new averaged price of your holdings (avg price = amount invested/number of shares)
    portfolio.Average_Price[index] = round(portfolio.Amount_Invested[index]/portfolio.Shares[index], 2)

    # Update the modified date
    portfolio.Date_Last_Modified[index] = mod_date

    # Sort the stocks based on their tickers
    portfolio = portfolio.reindex(index=order_by_index(portfolio.index, index_natsorted(portfolio['Ticker'])))
    portfolio.to_csv(portfolio_dir+portfolio_name, header=True, index=False)

    return

# Load up the dedired portfolio
portfolio_dir = './Portfolios/'
portfolio_name = 'stash_portfolio' + '.csv'

portfolio = pd.read_csv(portfolio_dir + portfolio_name, engine='python')

# Modify stocks in the portfolio
add_action = str(input('\nDo you want to modify stocks in your porfolio? (y/n): '))

while add_action == 'y':
    add_shares(portfolio, portfolio_dir, portfolio_name)
    add_action = str(input('\nDo you want to modify more stocks in your porfolio? (y/n): '))

    if add_action == 'n': break
