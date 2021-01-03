# Quiver Quantitative Alternative Data
This package allows you to access several alternative data sources which are updated daily and mapped to tickers. These include:
- Trading by US congressmen
- Corporate Lobbying
- Government Contracts
- Companies' Wikipedia page views
- Discussions on Reddit's /r/WallStreetBets

This data can be used for backtesting and implementing trading strategies.

### Receiving API Token
You can sign up for a Quiver API token [here](https://api.quiverquant.com). 

The cost is $10/month, please [e-mail me](mailto:chris@quiverquant.com) if that is an issue and I may be able to help cover.

## Getting Started
#### Prerequisites
- Python version 3 installed locally
- Pip installed locally

#### Installation
The package can easily be installed in your terminal by entering
```python
pip install quiverquant
```

### Usage
```python
#Import the package
import quiverquant

#Connect to the API using your token
#Replace <TOKEN> with your token
quiver = quiverquant.quiver("<TOKEN>")

#Get recent trades by members of U.S. Congress
dfCongress = quiver.congress_trading()

#Get trades of a Tesla by members of congress
dfCongress_Tesla = quiver.congress_trading("TSLA")

#Get trades made by U.S. Senator Richard Burr
dfCongress_Burr = quiver.congress_trading("Richard Burr", politician=True)

#Get data on WallStreetBets discussion
dfWSB = quiver.wallstreetbets()

#Get data on WallStreetBets discussion of Virgin Galactic
dfWSB_Virgin = quiver.wallstreetbets("SPCE")

#Get recent corporate lobbying
dfLobbying = quiver.lobbying()

#Get corporate lobbying by Apple
dfLobbying_Apple = quiver.lobbying("AAPL")

#Get data on government contracts
dfContracts = quiver.gov_contracts()

#Get data on government contracts to Lockheed Martin
dfContracts_Lockheed = quiver.gov_contracts("LMT")

#Get data on Wikipedia page views
dfWiki = quiver.wikipedia()

#Get data on Wikipedia page views of Microsoft
dfWiki_Microsoft = quiver.wikipedia("MSFT")
```


