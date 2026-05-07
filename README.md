# Quiver Quantitative Alternative Data
This package allows you to access several alternative data sources which are updated daily and mapped to tickers. These include:
- Trading by US congressmen
- Corporate Lobbying
- Government Contracts
- Insider Transactions
- Hedge Fund Moves
- Executive Compensation
- Corporate Election Donations
- Patents
- Off-exchange short volume
- Companies' Wikipedia page views
- Discussion on Reddit's r/wallstreetbets
- Companies' Twitter followings
- Flights by corporate private jets


This data can be used for backtesting and implementing trading strategies.

You can find full documentation on the Quiver Quantitative API [here](https://api.quiverquant.com/docs/).

### Receiving API Token
You can sign up for a Quiver API token [here](https://api.quiverquant.com). 

The pricing starts at $30/month, please [e-mail me](mailto:chris@quiverquant.com) if that is an issue and I may be able to help cover.

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




#Get the most recent stock news (across all tickers)
dfNews = quiver.news()


#Get the most recent Oracle stock news
dfNews_oracle = quiver.news(ticker="ORCL")


#Get recent trades by members of U.S. Congress
dfCongress = quiver.congress_trading()

#Get trades of a Tesla by members of congress
dfCongress_Tesla = quiver.congress_trading("TSLA")

#Get trades made by U.S. Senator Richard Burr
dfCongress_Burr = quiver.congress_trading("Richard Burr", politician=True)

#Get data on recent insider transactions
dfInsiders = quiver.insiders()

#Get data on recent insider transactions by Tesla insiders
dfInsiders_Tesla = quiver.insiders("TSLA")


#Get data on recent hedge fund moves in Amazon
df13F_Amazon = quiver.sec13FChanges(ticker="AMZN")

#Get data on holdings in Situational Awareness' portfolio
df13F_fund = quiver.sec13F(owner="Situational Awareness LP")


#Get data on the top Walmart shareholders
dfShareholders_Walmart = quiver.top_shareholders(ticker="WMT")

#Get data on executive compensation at Nvidia
dfCompensation_Nvidia = quiver.executive_compensation(ticker='NVDA')

#Get data on election donations by Chevron
dfDonations_Chevron = quiver.corporate_donors(ticker="CVX")


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


#Get data on patents by Apple
dfPatents_Apple = quiver.patents("AAPL")


```


