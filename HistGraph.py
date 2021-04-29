import matplotlib.pyplot as plt
import pandas as pd
pd.options.mode.chained_assignment = None
import datetime
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import csv
import sklearn.model_selection as sk
import numpy as np
##from plotly.subplots import make_subplots
from db_connect import mysql as ms
class HistGraph():
    def __init__(self,coi):
        coin = coi  # input("Enter coin")
        self.sql = ms()
        currencies = self.sql.currencies
        coin = currencies[coi][0]
        start = currencies[coi][1]
        df1 = pd.read_csv('Poloniex_{}USDT_1h.csv'.format(coin))
        d1 = datetime.datetime.strptime('2021-03-30 00:00:00', "%Y-%m-%d %H:%M:%S")
        d2 = datetime.datetime.strptime('{} 00:00:00'.format(start), "%Y-%m-%d %H:%M:%S")
        # print(d1,type(d2))
        d1 = pd.Timestamp(d1)
        d2 = pd.Timestamp(d2)
        df1['date'] = pd.to_datetime(df1['date'])
        df = df1[(df1['date'] < d1) & (df1['date'] > d2)]
        df.set_index(df['date'])
        # print(df.head())

        df['Volume USDT'] = pd.to_numeric(df['Volume USDT'])
        df['high'] = pd.to_numeric(df['high'])

        max_value = df['Volume USDT'].max()
        min_value = df['Volume USDT'].min()
        df['Volume USDT norm'] = (df['Volume USDT'] - min_value) / (max_value - min_value)
        df['Volume USDT avg'] = df['Volume USDT'].rolling(window=10).mean()

        df['mav'] = df['high'].rolling(window=100, center=True).mean()
        df['ma'] = df['high'].rolling(window=10, center=True).mean()
        df['ms'] = df['high'].rolling(window=8).std()
        df['anomaly'] = df['high'].copy()
        df['diff'] = df['ma'].diff() * 100
        df['diff2'] = df['diff'].diff()
        df['diffvar'] = df['diff2'].rolling(window=8).std()
        df['diffvaravg'] = df['diffvar'].rolling(window=100).mean()
        df['high+1'] = df['high'].shift(-1)
        # print(df.head(100))
        df.loc[(df['high'] < df['mav']) | (df['diffvar'] < df['diffvaravg']) | (df['diff2'] <= 0) | (
                    df['high+1'] > df['high']), 'anomaly'] = np.nan  #
        dfb = df[['anomaly', 'date']].copy()

        dfb.dropna(inplace=True)

        dfb['date'] = dfb['date'].apply(lambda x: x.value)
        # print(dfb.head())
        ano = []
        indices = []
        dates = []
        c = 0
        for i in dfb.index:
            indices.append(i)
            dates.append(dfb['date'][i])
            c += 1
        ana_clust = dfb
        ana_clust = StandardScaler().fit_transform(ana_clust)
        db = DBSCAN(eps=0.025, min_samples=2).fit(ana_clust)
        labels = list(db.labels_)

        prices = []
        for i in indices:
            prices.append(df['high'].loc[df.index == i].values[0])

        anomally_list = pd.DataFrame(
            {'index': indices,
             'date': dates,
             'labels': labels,
             'price': prices
             })
        cluster_price = anomally_list.groupby(['labels'])['price'].max()
        cluster_index = anomally_list.groupby(['labels'])['index'].median()
        cluster_date = pd.to_datetime(anomally_list.groupby(['labels'])['date'].median())
        ax1 = plt.subplot()
        ax2 = ax1.twinx()
        ax1.plot_date(df['date'], df['high'], color='#000000', label='price',linestyle="solid",marker ="None")
        ax1.plot_date(df['date'], df['mav'], color='#888888', label='price',linestyle="solid",marker ="None")
        ax1.plot_date(df['date'], df['anomaly'], marker='.', color='#FFFF00',linestyle="None")
        ax1.plot(cluster_date, cluster_price, marker='^', linestyle="None", color='#FF0000')
        ax2.plot(df['date'], df['Volume USDT'], color='#00FF00')
        ax2.set_yticks([0, 1 * max_value, 2 * max_value, 3 * max_value, 4 * max_value])
        ax1.set_ylabel('Price vs USD')
        ax2.set_ylabel('Volume in Thousands')
        ax1.set_xlabel('Time->')
        plt.title('{} VS USD'.format(coin))
        plt.show()