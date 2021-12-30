This repository focuses on the analysis of a stocks portfolio.
The idea is that one can create its own portfolio and edit it as one pleases.
The codes will keep track of stock progress in the market, dividends payouts and dates,
as well as diversification of the portfolio.
We primarily use the Python module yfinance (https://pypi.org/project/yfinance/)
to keep up with the stock prices and perform the basic portfolio analysis

This is how the codes in this repository work:

my_portfolio.py
Creates the user's stock portfolio by creating a csv file with the following information:
- Stock Ticker
- Company's long name
- Number of shares the user owns
- Average price of the investments
- Amount invested in each individual stock
- Last date the user modified the portfolio
