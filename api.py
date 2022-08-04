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
# the website is formatted in f-strings which allows the website to be adjusted based on the parameters above
# if a different currency exchange is required, it can be simply be changed from the parameters above, no need to change from the website itself
    url = f'https://www.alphavantage.co/query?function={function}&from_currency={from_symbol}&to_currency={to_symbol}&apikey={apikey}'

# request.get() function sends a GET request to the specific url
# .json() function returns the request to a JSON object
# it is then assigned to the variable 'data'
    data = requests.get(url).json()

# returns and end back to the define function, to execute the code above
# return the desired currency exchange rate part of the nested list using data['Realtime Currency Exchange Rate']['5. Exchange Rate'] 
# float() function will convert the value to a float number
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
