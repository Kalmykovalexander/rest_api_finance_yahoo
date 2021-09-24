import requests
import datetime, time
import pandas as pd
import sqlite3
from rest_framework import generics
from .models import FinanceData
from .serializers import FinanceListSerializer


# Get finance historical data from Yahoo
def get_finance_data(ticker):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36'
    }
    period_to = int(time.mktime(datetime.datetime.now().timetuple()))
    base_url = f'https://query2.finance.yahoo.com/v8/finance/chart/{ticker}' \
               f'?formatted=true&crumb=5uzj3cy61Nk&lang=en-US&region=US&includeAdjustedClose=true&interval=1d&period1=0&period2={period_to}' \
               f'&events=capitalGain%7Cdiv%7Csplit&useYfid=true&corsDomain=finance.yahoo.com'
    response = requests.get(base_url, headers=headers)
    data = response.json()

    symbol = data['chart']['result'][0]['meta']['symbol']
    timestamp = data['chart']['result'][0]['timestamp']
    date = [datetime.datetime.fromtimestamp(i).date() for i in timestamp]
    open = data['chart']['result'][0]['indicators']['quote'][0]['open']
    high = data['chart']['result'][0]['indicators']['quote'][0]['high']
    low = data['chart']['result'][0]['indicators']['quote'][0]['low']
    close = data['chart']['result'][0]['indicators']['quote'][0]['close']
    adjclose = data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    volume = data['chart']['result'][0]['indicators']['quote'][0]['volume']

    df = pd.DataFrame({'symbol': symbol,
                       'date': date,
                       'open': open,
                       'high': high,
                       'low': low,
                       'close': close,
                       'adj_close': adjclose,
                       'volume': volume})

    return df


# Insert data to sqlite database
def insertDb(data):
    try:
        con = sqlite3.connect("db.sqlite3")
        data.index += 1
        data.to_sql(
            'historical_data_financedata',
            con=con,
            if_exists="replace",
            index_label='id'
        )
        con.commit()
        con.close()
    except Exception as e:
        print(e)


# View for display historical data
class FinanceListView(generics.ListAPIView):
    serializer_class = FinanceListSerializer
    http_method_names = ['get']

    def get_queryset(self):
        """
        GET
        """
        if self.request.method == 'GET':
            symbol_slug = self.kwargs['ticker_slug']
            if symbol_slug is not None:
                # Get data by symbol from Finance Yahoo
                data = get_finance_data(symbol_slug)
                # Insert data to database
                insertDb(data)
                queryset = FinanceData.objects.all()
        return queryset

