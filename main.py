from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from IPython.display import JSON


api_key = "XXXXXXXX"
api_secret = "XXXXXXXX"
capital = 1000
if __name__ == '__main__':
    client = Client(api_key, api_secret)
    trades = (client.futures_income_history(incomeType="REALIZED_PNL", startTime=1627855200000, limit=999))
    listOfCapitals = []
    for trade in trades:
        capital += float(trade["income"])
        listOfCapitals.append(capital)
    
    series = pd.Series(listOfCapitals)
    series.plot()
    plt.show()
    print(json.dumps(trades, indent=2))
