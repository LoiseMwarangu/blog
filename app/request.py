import requests

def random_quote():
    url='http://quotes.stormconsultancy.co.uk/random.json'
    quo= requests.get(url)
    quote= quo.json()
    return quote