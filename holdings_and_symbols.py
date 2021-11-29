import requests
from bs4 import BeautifulSoup

mainPage = "https://www.dataroma.com/"
managers = "https://www.dataroma.com/m/managers.php"
allHoldings = {}
allTickers = set()

agentHeader = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

def allCurrentHoldings():
    response = requests.get(url=managers, headers=agentHeader)
    superInvestorsPage = BeautifulSoup(response.content, 'html.parser')
    managerTable = BeautifulSoup(str(superInvestorsPage.find("tbody")), 'html.parser')
    for manager in managerTable.findAll("td", class_="man"):
        investor, shares = pullHoldings(mainPage + manager.a.get('href'))
        allHoldings[investor] = shares
    return allHoldings, allTickers
    


def pullHoldings(link):
    response = requests.get(url=link, headers=agentHeader)
    managerPage = BeautifulSoup(response.content, 'html.parser')
    investor = managerPage.find(id='f_name').get_text()
    tickerTable = BeautifulSoup(str(managerPage.find("tbody")), 'html.parser')
    holdings = {}
    for ticker in tickerTable.findAll("td", class_="stock"):
        symbol = ticker.a.get_text().split(" ", 1)[0]
        sharesHeld = ticker.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        allTickers.add(symbol)
        holdings[symbol] = sharesHeld
    return investor, holdings
    
    
if __name__ == '__main__':
    allCurrentHoldings()
    print(len(allTickers))
    # pullHoldings('https://www.dataroma.com/m/holdings.php?m=AKO')   