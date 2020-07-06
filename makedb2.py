import csv, sqlite3
import pandas as pd

conn = sqlite3.connect('./test6.db')
df = pd.read_csv('./Orthopaedic_Edvice_Reference2.csv')
df.to_sql('test1', conn, if_exists='append', index=False)