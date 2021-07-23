import sqlite3

connect = sqlite3.connect('../db.sqlite3')

#import pandas as pd

df = pd.read_sql_query('select * from  dbapp_economic de', connect)

# print(df.head(4))