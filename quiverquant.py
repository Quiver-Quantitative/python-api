import requests
import json
import pandas as pd

class quiver:
    def __init__(self, token):
        self.token = token
        self.headers = {'accept': 'application/json',
        'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
        'Authorization': "Token "+self.token}
    
    def congress_trading(self, ticker="", politician=False, recent=True):
        if recent:
            urlStart = 'https://api.quiverquant.com/beta/live/congresstrading'
        else:
            urlStart = 'https://api.quiverquant.com/beta/bulk/congresstrading'
        if politician:
            ticker = ticker.replace(" ", "%20")
            url = urlStart+"?representative="+ticker
            
        elif len(ticker)>0:
            urlStart = 'https://api.quiverquant.com/beta/historical/congresstrading'
            url = urlStart+"/"+ticker
        else:
            url = urlStart
        print(url)
        r = requests.get(url, headers=self.headers)
        j = json.loads(r.content)
        df = pd.DataFrame(j)
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        
        for col in ['ReportDate', 'TransactionDate', 'Filed', 'Traded', 'last_modified']:
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                continue

        return df
   

    def senate_trading(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/senatetrading/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/senatetrading"
        r = requests.get(url, headers=self.headers)
        j = json.loads(r.content)
        df = pd.DataFrame(j)
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df["Date"] = pd.to_datetime(df["Date"])
        return df

    def house_trading(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/housetrading/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/housetrading"
        r = requests.get(url, headers=self.headers)
        j = json.loads(r.content)
        df = pd.DataFrame(j)
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df["Date"] = pd.to_datetime(df["Date"])
        return df    
    
    def offexchange(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/offexchange/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/offexchange"
        r = requests.get(url, headers=self.headers)
        j = json.loads(r.content)
        df = pd.DataFrame(j)
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        if len(ticker)>0:
            df["Date"] = pd.to_datetime(df["Date"])
            
        return df
    
    def gov_contracts(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/govcontractsall/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/govcontractsall"

        r = requests.get(url, headers=self.headers)
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df

    
    def lobbying(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/lobbying/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/lobbying"

        r = requests.get(url, headers=self.headers)
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df["Date"] = pd.to_datetime(df["Date"])
        return df
        
    def insiders(self, ticker=""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/live/insiders?ticker="+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/insiders"
         
        print("Drawing from: ", url)
        r = requests.get(url, headers=self.headers)
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
       # df["Date"] = pd.to_datetime(df["Date"])
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
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df
    
    
    
    
    def news(self, ticker="", page_size="", page=""):
        payload = {
            "ticker": ticker,
            "page_size": page_size,
            "page": page
        }

        payload = {k: v for k, v in payload.items() if v != ""}

        url = "https://api.quiverquant.com/beta/live/quivernews"
        r = requests.get(url, headers=self.headers, params=payload)
        j = json.loads(r.content)['data']
        df = pd.DataFrame(j)
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        try:
            df['time'] = pd.to_datetime(df['time'])
        except:
            pass

        return df
    
    
    def top_shareholders(self, ticker):
        url = "https://api.quiverquant.com/beta/live/topshareholders/"+ticker
        print(url)

        r = requests.get(url, headers=self.headers)
        df = pd.DataFrame(json.loads(r.content)['ownership'])
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df
    

    
    def executive_compensation(self, ticker, page_size="", page=""):
        payload = {
            "page_size": page_size,
            "page": page
        }

        # Remove empty values
        payload = {k: v for k, v in payload.items() if v != ""}

        url = "https://api.quiverquant.com/beta/historical/executivecompensation/"+ticker
        print(url)

        r = requests.get(url, headers=self.headers, params=payload)
        df = pd.DataFrame(json.loads(r.content)['data'])
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df
    
 


    def corporate_donors(self, ticker="", bioguide_id="", cycle="", transaction_tp="", page_size="", page=""):
        payload = {
            "ticker": ticker,
            "bioguide_id": bioguide_id,
            "cycle": cycle,
            "transaction_tp": transaction_tp,
            "page_size": page_size,
            "page": page
        }

        payload = {k: v for k, v in payload.items() if v != ""}

        url = "https://api.quiverquant.com/beta/bulk/corporatedonors"
        r = requests.get(url, headers=self.headers, params=payload)

        j = json.loads(r.content)['data']
        df = pd.DataFrame(j)
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        try:
            df['Uploaded'] = pd.to_datetime(df['Uploaded'])
            df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
        except:
            pass

        return df
    
    
    def wallstreetbets(self, ticker="",date_from = "", date_to = "", yesterday=False):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/wallstreetbets/"+ticker

        else:
            url = "https://api.quiverquant.com/beta/live/wallstreetbets?count_all=true"

            if len(date_from)>0:
                date_from = pd.to_datetime(date_from).strftime('%Y%m%d')
                url = url+"&date_from="+date_from 
            if len(date_to)>0:
                url = url+"&date_to="+date_to 

        if yesterday:
            url = "https://api.quiverquant.com/beta/live/wallstreetbets"

        print(url)
        r = requests.get(url, headers=self.headers)

        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')

        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        
        if not yesterday:
            try:
                df["Date"] = pd.to_datetime(df["Time"], unit='ms')
            except:
                df["Date"] = pd.to_datetime(df["Date"]) 
            if len(date_from)>0:
                df = df[df["Date"]>=pd.to_datetime(date_from)]
            if len(date_to)>0:
                df = df[df["Date"]<=pd.to_datetime(date_to)]

        return df 
    
    def twitter(self, ticker = ""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/twitter/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/twitter"

        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df 
    
    def spacs(self, ticker = ""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/spacs/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/spacs"

        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df 
    
    def flights(self, ticker = ""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/flights/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/flights"

        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df 
        
        
    def political_beta(self, ticker = ""):
        if len(ticker)>0:
            url = "https://api.quiverquant.com/beta/historical/politicalbeta/"+ticker
        else:
            url = "https://api.quiverquant.com/beta/live/politicalbeta"

        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        return df 
    
    def patents(self, ticker = ""):
        if len(ticker)<1:
            url = "https://api.quiverquant.com/beta/live/allpatents"
        else:
            url = "https://api.quiverquant.com/beta/historical/allpatents/"+ticker
       
        print("Pulling data from: ", url)
        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
        
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df["Date"] = pd.to_datetime(df["Date"])
        
        return df
    
    ## Contact chris@quiverquant.com about access to these functions
    def sec13F(self, ticker="", date="", owner="", period=""):
        separator = "?"
        url = "https://api.quiverquant.com/beta/live/sec13f"
        if len(ticker)>0:
            url = url+separator+"ticker="+ticker
            separator = "&"
        if len(date)>0:
            url = url+separator+"date="+date
            separator = "&"
        if len(owner)>0:
            url = url+separator+"owner="+owner
            separator="&"
        if len(period)>0:
            url = url+separator+"period="+period
            separator="&"
            
        print("Pulling data from: ", url)     
        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df["ReportPeriod"] = pd.to_datetime(df["ReportPeriod"])
        df["Date"] = pd.to_datetime(df["Date"])       
        return df
    
    def sec13FChanges(self, ticker="", date="", owner="", period=""):
        separator = "?"
        url = "https://api.quiverquant.com/beta/live/sec13fchanges"
        if len(ticker)>0:
            url = url+separator+"ticker="+ticker
            separator = "&"
        if len(date)>0:
            url = url+separator+"date="+date
            separator = "&"
        if len(owner)>0:
            url = url+separator+"owner="+owner
            separator="&"
        if len(period)>0:
            url = url+separator+"period="+period
            separator="&"
            
        print("Pulling data from: ", url)     
        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df["ReportPeriod"] = pd.to_datetime(df["ReportPeriod"])

        df["Date"] = pd.to_datetime(df["Date"])       
        return df    
    
    def wallstreetbetsComments(self, ticker="", freq="", date_from = "", date_to = ""):
        separator = "?"
        url = "https://api.quiverquant.com/beta/live/wsbcomments"
        if len(ticker)>0:
            url = url+separator+"ticker="+ticker
            separator = "&"
        if len(freq)>0:
            url = url+separator+"freq="+freq
            separator = "&"
        if len(date_from)>0:
            url = url+separator+"date_from="+date_from
            separator = "&"   
        if len(date_to)>0:
            url = url+separator+"date_to="+date_to
            separator = "&"   
            
        print("Pulling data from: ", url)
        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset. Contact chris@quiverquant.com with questions.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        #df['Datetime'] = pd.to_datetime(df["Time"], unit='ms')
        return df 
    
    def wallstreetbetsCommentsFull(self, ticker="", freq="", date_from = "", date_to = ""):
        separator = "?"
        url = "https://api.quiverquant.com/beta/live/wsbcommentsfull"
        if len(ticker)>0:
            url = url+separator+"ticker="+ticker
            separator = "&"
        if len(freq)>0:
            url = url+separator+"freq="+freq
            separator = "&"
        if len(date_from)>0:
            url = url+separator+"date_from="+date_from
            separator = "&"   
        if len(date_to)>0:
            url = url+separator+"date_to="+date_to
            separator = "&"   
            
        print("Pulling data from: ", url)
        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset. Contact chris@quiverquant.com with questions.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df['Datetime'] = pd.to_datetime(df["Time"], unit='ms')
        return df 
    
       
    def cryptoComments(self, ticker="", freq="", date_from = "", date_to = ""):
        separator = "?"
        url = "https://api.quiverquant.com/beta/live/cryptocomments"
        if len(ticker)>0:
            url = url+separator+"ticker="+ticker
            separator = "&"
        if len(freq)>0:
            url = url+separator+"freq="+freq
            separator = "&"
        if len(date_from)>0:
            url = url+separator+"date_from="+date_from
            separator = "&"   
        if len(date_to)>0:
            url = url+separator+"date_to="+date_to
            separator = "&"   
            
        print("Pulling data from: ", url)
        r = requests.get(url, headers=self.headers)
        
        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset. Contact chris@quiverquant.com with questions.')
            
        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df['Datetime'] = pd.to_datetime(df["Time"], unit='ms')
        return df 
    
    def cryptoCommentsHistorical(self, ticker="", freq="", date_from = "", date_to = ""):
        separator = "?"
        url = "https://api.quiverquant.com/beta/live/cryptocommentsfull"
        if len(ticker)>0:
            url = url+separator+"ticker="+ticker
            separator = "&"
        if len(freq)>0:
            url = url+separator+"freq="+freq
            separator = "&"
        if len(date_from)>0:
            url = url+separator+"date_from="+date_from
            separator = "&"   
        if len(date_to)>0:
            url = url+separator+"date_to="+date_to
            separator = "&"   

        print("Pulling data from: ", url)
        r = requests.get(url, headers=self.headers)

        if r.text == '"Upgrade your subscription plan to access this dataset."':
            raise NameError('Upgrade your subscription plan to access this dataset. Contact chris@quiverquant.com with questions.')

        df = pd.DataFrame(json.loads(r.content))
        if (len(df)==0) or (df.shape[0]==0):
            print("No results found")
            return df
        df['Datetime'] = pd.to_datetime(df["Time"], unit='ms')
        return df 
