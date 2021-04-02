import pandas as pd
import numpy as np
def calculate_statistics(df, ticket_ids): #df-dataFrame ticket_ids - list
    df1 = df.set_index('ticket_id')
    dict1 ={}
    #filtr_df = df[df['ticket_id'].isin([ticket_ids])]
    filtr_df = df1.loc[ticket_ids]
    print(filtr_df)
    dict1['mean'] = np.mean(filtr_df['price'])
    dict1['median'] = np.median(filtr_df['price'])
    dict1['std'] = np.std(filtr_df['price'], ddof=1)
    return(dict1)

mas = []
list1 = input().split(",")
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
mas.append(input().split(","))
print(list1)
print(calculate_statistics(mas,list1))