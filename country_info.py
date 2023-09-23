import requests
import json
from pprint import pprint
from countryinfo import CountryInfo



while True:
    count = input('Enter a country: ')
    country = CountryInfo(count)
    info = country.info()
    if count == 'stop':
        break
    try:
     languages = info['languages']
     capital = info['capital']
     currencies = info['currencies']
     ISO = info ['ISO']['alpha2']
     region = info ['region']

     print(f'''
capital: {capital}
languages:{languages}
currencies: {currencies}
ISO:{ISO}
region: {region}
''')

    except:
        print('country not found')
