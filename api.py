# import the requests module library
# allows to send HTTP requests using python to get response objects
import requests

# create a define function: api_function
def api_function():

# based on the assignment brief, create the following API parameters
# the parameters are made to extract the real time exchange rate (Forex)
# api key is taken from the alphavantage.co website
    function = 'CURRENCY_EXCHANGE_RATE'
    from_symbol = 'USD'
    to_symbol = 'SGD'
    apikey = 'HOG9MJHJFP1H7D5D'

# alphavantage website assigned to 'url' variable
# the website is formatted in f-strings
# f-strings allows the website to be adjusted based on the parameters above
# if the automation needs to change the currency used, it can just simply change from the parameters above automatically, it does not have to change from the website it self
    url = f'https://www.alphavantage.co/query?function={function}&from_currency={from_symbol}&to_currency={to_symbol}&apikey={apikey}'

# function request.get() sends a GET request to the specific url
# function .json() returns the request to a JSON object
# it is then assigned to the variable 'data'
    data = requests.get(url).json()

# returns and end back to the define function, to execute the code above
# it will return a specific part of the nested list gotten from requesting the data
# data['Realtime Currency Exchange Rate']['5. Exchange Rate'] will only get the values corresponding to the specific list content
# float() of the return list value will convert the value to a float number
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

# below is an example of what 'data' requests and returns:
# {'Realtime Currency Exchange Rate': 
# {'1. From_Currency Code': 'USD', 
# '2. From_Currency Name': 'United States Dollar', 
# '3. To_Currency Code': 'SGD', 
# '4. To_Currency Name': 'Singapore Dollar', 
# '5. Exchange Rate': '1.37792000', 
# '6. Last Refreshed': '2022-08-04 13:49:01', 
# '7. Time Zone': 'UTC', 
# '8. Bid Price': '1.37792000', 
# '9. Ask Price': '1.37792000'}}

# return(float(data['Realtime Currency Exchange Rate']['5. Exchange Rate']) will get the values corresponding to it