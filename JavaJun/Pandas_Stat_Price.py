import math

import pandas as pd
import numpy as np
def calculate_statistics(df):
    for i in range(len(df)):
        if (i > 0):
            for j in range(len(df[i])):
                if df[i][j] == '':
                    df[i][j] = None
    df = pd.DataFrame(df,
                      columns=[df[0][0], df[0][1]])
    dict1 ={}
    a = df['price'].tolist()
    dict1['mean'] = np.mean(df['price'])
    dict1['median'] = np.median(df['price'])
    dict1['std'] = np.std(df['price'], ddof=1)
    mean = np.mean(df['price'])
    pos = len(a) // 2
    med = sorted(a)[pos - 1]
    sumNew = 0
    for i in range(len(a)):
        if (i > 0):
            sumNew = sumNew + (float(a[i]) - mean)*(float(a[i])-mean)
    print(sumNew)
    std = math.sqrt(sumNew/(len(a) - 2))
    dict1["mean"] = round(mean,2)
    dict1["median"] = med
    dict1["std"] = round(std,2)
    return(dict1)

mas = []
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
print(calculate_statistics(mas))