import requests
import json
import pandas as pd

class quiver:
    def __init__(self, token):
        self.token = token
        self.headers = {'accept': 'application/json',
        'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
        'Authorization': "Token "+self.token}
    
    def congress_trading(self, ticker="", politician=False):
        if politician:
            ticker = ticker.replace(" ", "%20")
            url = "https://api.quiverquant.com/beta/live/congresstrading?representative="+ticker
            
        elif len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/congresstrading/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/congresstrading"+ticker
        print(url)
        r = requests.get(url, headers=self.headers)
        j = json.loads(r.content)
        df = pd.DataFrame(j)
        return df
    
    def gov_contracts(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/govcontracts/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/govcontracts"

        r = requests.get(url, headers=self.headers)
        df = pd.DataFrame(json.loads(r.content))
        return df

    
    def lobbying(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/lobbying/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/lobbying"

        r = requests.get(url, headers=self.headers)
        df = pd.DataFrame(json.loads(r.content))
        return df
        

    def wikipedia(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/wikipedia/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/wikipedia"

        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        return df
    
    def wallstreetbets(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/wallstreetbets/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/wallstreetbets"

        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        return df 
    

  
