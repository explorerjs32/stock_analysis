import numpy as np
import pandas as pd
import yfinance as yf
import os
from datetime import date
from natsort import natsorted, index_natsorted, order_by_index


def add_to_portfolio(portfolio, portfolio_dir, portfolio_name):
    print('Add new stocks to your portfolio:\n')
    # Chose a ticker and extract the information
    ticker = str(input('What is the stock Ticker? '))

    if ticker in portfolio['Ticker']:
        pass
        return

    else:
        name = yf.Ticker(ticker).info['longName']
        shares = round(float(input('How many shares do you have? ')), 5)
        avg_price = float(input('What is the average price? '))
        amt_invested = float(input('How much have you invested? '))
        date_mod = date.today().strftime("%Y-%m-%d")

        # Add the stock info to the portfolio
        new_row = [ticker, name, shares, avg_price, amt_invested, date_mod]
        portfolio.loc[len(portfolio.index)] = new_row

        # Sort the stocks based on their tickers
        portfolio = portfolio.reindex(index=order_by_index(portfolio.index, index_natsorted(portfolio['Ticker'])))
        portfolio.to_csv(portfolio_dir+portfolio_name, header=True, index=False)

        return


# Start by loading up the portfolio information
# If the portfolio does not exist, then let's create one
portfolio_dir = './Portfolios/'
portfolio_name = str(input('Enter your portfolio name: ')) + '.csv'

if not os.path.isdir(portfolio_dir):
    # Create the directory to store the portfolios
    os.mkdir(portfolio_dir)

# Check if the portfolio file exists
if not os.path.isfile(portfolio_dir+portfolio_name):
    # Create the data sheet of my portfolio
    table_cols = ['Ticker', 'Name', 'Shares', 'Average_Price', 'Amount_Invested', 'Date_Last_Modified']
    portfolio = pd.DataFrame(data=None, columns=table_cols)

    portfolio.to_csv(portfolio_dir+portfolio_name, header=True, index=False)

# Load up the pportfolio data
portfolio = pd.read_csv(portfolio_dir + portfolio_name, engine='python')

# Add stocks to the portfolio
add_action = str(input('\nDo you want to add stocks to your porfolio? (y/n): '))

while add_action == 'y':
    add_to_portfolio(portfolio, portfolio_dir, portfolio_name)
    add_action = str(input('\nDo you want to add more stocks to your porfolio? (y/n): '))

    if add_action == 'n': break
