import pandas as pd
import numpy as np
def find_null_columns(df):
    for i in range(len(df)):
        if (i > 0):
            for j in range(len(df[i])):
                if df[i][j] == '':
                    df[i][j] = None
    df = pd.DataFrame(df,
                      columns=[df[0][0], df[0][1], df[0][2], df[0][3]])
    b = df.dropna(axis=0)
    b = b[b.index > 0]
    #b.drop(labels=None, axis=0, index=0, columns=None, level=None, inplace=False, errors='raise')
    print(b)
    c = np.nanmean(b['price'])
    print(c)
    df.fillna(c)
    return (df)

mas = []
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
find_null_columns(mas)