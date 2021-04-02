import pandas as pd
import numpy as np
def find_nearest(df, price):
    for i in range(len(df)):
        if (i > 0):
            for j in range(len(df[i])):
                if df[i][j] == '':
                    df[i][j] = None
    df = pd.DataFrame(df,
                      columns=[df[0][0], df[0][1], df[0][2], df[0][3]])
    df_sort = df.iloc[(df['price'] - float(price)).abs().argsort()[:2]]
    print(df_sort)

    def find_nearest(df, price):
        price = float(price)
        mas = str(df['ticket_id'].iloc[(df['price'] - price).abs().argsort()[0:1]] + "," + df['flight_id'].iloc[
            (df['price'] - price).abs().argsort()[0:1]] + "," + df['operator_id'].iloc[
                      (df['price'] - price).abs().argsort()[0:1]] + "," + str(
            df['price'].iloc[(df['price'] - price).abs().argsort()[0:1]]))
        print(mas)
        df2 = pd.Series(data=[mas], index=range(1))
        return (df2)

price = input()
mas = []
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
find_nearest(mas, price)