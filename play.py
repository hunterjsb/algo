import requests
import datetime as dt
import json
import time
import matplotlib.pyplot as plt
import pandas as pd
from vehicles.stock import Stock, LocalStock

# CONSTANTS
KEY = None  # ADD KEY
APD = 16847.611650485436  # average WSB per day since dec 01, 2019

# VARS
today = dt.datetime.today().strftime('%Y-%m-%d')
two_years_ago = (dt.datetime.today() - dt.timedelta(365 * 2)).strftime('%Y-%m-%d')


def graph_subs_volume_price(stonk: LocalStock, sub='wallstreetbets', vol_scale=10000, price_scale=5000):
    df = stonk.compare_to_sub(sub)

    # VARS
    # volumes = df['v']/vol_scale
    wsb = df['subs']/APD
    wsb_per_day = df['subs'].diff()
    # prices = df['c']*price_scale

    # PLOT
    plt.plot(wsb, color='r')
    plt.plot(wsb_per_day, color='lime')
    # plt.bar(volumes.index, volumes)
    # plt.plot(prices, color='g')
    plt.show()


# THEN play with the data
if __name__ == "__main__":
    graph_subs_volume_price(LocalStock('SNDL'))
