import pandas as pd
from pymongo import MongoClient

df = pd.read_excel('seoul.xls', header=0)

print(df)

client= MongoClient('localhost', 27017)
db= client['dbJMT']
collection = db['JMT']

collection.insert_many(df.to_dict('records'))

