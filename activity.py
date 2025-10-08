import pandas as pd, sqlite3
df = pd.read_csv("activity.csv")
conn =
sqlite3.connect("activity.db")
df.to_sql("activity_logs", conn,
if_exists="append", index=False)
