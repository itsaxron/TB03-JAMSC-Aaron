import requests
#Create a customised function to find the currency exchange rate
def api_function():

    function = 'CURRENCY_EXCHANGE_RATE'
    from_currency = 'USD'
    to_currency = 'SGD'
    apikey = 'HOG9MJHJFP1H7D5D'
    
    url = f'https://www.alphavantage.co/query?function={function}&from_currency={from_currency}&to_currency={to_currency}&apikey={apikey}'
    
    data = requests.get(url).json()
    
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
