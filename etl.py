# import holdings_and_symbols as superInvestors
import yfinance as yf
import webbrowser
import holdings_and_symbols as superInvestors

msft = yf.Ticker("MSFT")

hist = msft.history(period="max")

if __name__ == '__main__':
    holdings, tickers = superInvestors.allCurrentHoldings()
    
