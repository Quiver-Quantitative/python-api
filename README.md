# Quiver Quantitative Alternative Data
This package allows you to access several alternative data sources which are updated daily and mapped to tickers. These include:
- Trading by US congressmen
- Corporate Lobbying
- Government Contracts
- Patents
- Off-exchange short volume
- Companies' Wikipedia page views
- Discussion on Reddit's r/wallstreetbets
- Discussion on Reddit's r/SPACs
- Companies' Twitter followings
- Flights by corporate private jets
- Political Beta
- Insider Transactions

This data can be used for backtesting and implementing trading strategies.

### Receiving API Token
You can sign up for a Quiver API token [here](https://api.quiverquant.com). 

The pricing starts at $10/month, please [e-mail me](mailto:chris@quiverquant.com) if that is an issue and I may be able to help cover.

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

#Get data on WallStreetBets discussion
dfWSB = quiver.wallstreetbets()

#Get data on WallStreetBets discussion of GameStop
dfWSB_GameStop = quiver.wallstreetbets("GME")

#Get recent trades by members of U.S. Congress
dfCongress = quiver.congress_trading()

#Get trades of a Tesla by members of congress
dfCongress_Tesla = quiver.congress_trading("TSLA")

#Get trades made by U.S. Senator Richard Burr
dfCongress_Burr = quiver.congress_trading("Richard Burr", politician=True)

#Get recent corporate lobbying
dfLobbying = quiver.lobbying()

#Get corporate lobbying by Apple
dfLobbying_Apple = quiver.lobbying("AAPL")

#Get data on government contracts
dfContracts = quiver.gov_contracts()

#Get data on government contracts to Lockheed Martin
dfContracts_Lockheed = quiver.gov_contracts("LMT")

#Get data on off-exchange short volume
dfOTC = quiver.offexchange()

#Get data on off-exchange short volume for AMC
dfOTC_AMC = quiver.offexchange("AMC")

#Get data on Wikipedia page views
dfWiki = quiver.wikipedia()

#Get data on Wikipedia page views of Microsoft
dfWiki_Microsoft = quiver.wikipedia("MSFT")

#Get data on companies' Twitter following
dfTwitter = quiver.twitter()

#Get data on GE's Twitter following
dfTwitter_GE = quiver.twitter("GE")

#Get data on r/SPACs discussion
dfSPACs = quiver.spacs()

#Get data on r/SPACs discussion of CCIV
dfSPACs_CCIV = quiver.spacs("CCIV")

#Get data on recent corporate private jet flights
dfFlights = quiver.flights()

#Get data on private jet flights by Target
dfFlights_Target = quiver.flights("TGT")

#Get data on patents by Apple
dfPatents_Apple = quiver.patents("AAPL")

#Get data on recent insider transactions
dfInsiders = quiver.insiders()

#Get data on recent insider transactions by Tesla insiders
dfInsiders_Tesla = quiver.insiders("TSLA")
```


