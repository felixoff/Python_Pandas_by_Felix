import pandas as pd
import numpy as np
def find_null_columns(df):
    for i in range(len(df)):
        if (i > 0):
            for j in range(len(df[i])):
                if df[i][j] == '':
                    df[i][j] = None
    df = pd.DataFrame(df,
                      columns=[df[0][0], df[0][1], df[0][2]])
    print(df)
    a = df.columns.values
    b = df.dropna(axis=0)
    print(b)
    c =list(set(a) - set(b))
    for i in range(len(c) - 1):
        print(c[i], end=",")
    if (len(c) > 0):
        print(c[len(c) - 1])
    return([i for i in a if i in c])

mas = []
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
find_null_columns(mas)