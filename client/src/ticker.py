from yahoofinancials import YahooFinancials
import os 
import datetime 


class GetData():

    def __init__(self) -> None:
        pass


    def get_historical_price() -> None:
        pass

    with open(f'{os.path.dirname(__file__)}/ticker.txt','r') as file:
        tickers = [x.replace('\n','') for x in file.readlines()]  #This process need to be improved in the future 


    yahoo_financials = YahooFinancials(tickers, concurrent=True, max_workers=8, country="US")

    file.close() #

    historical_price = yahoo_financials.get_historical_price_data(
        start_date='1900-01-01',
        end_date= str(datetime.datetime.now().date()),
        time_interval='daily')

    print('lol')