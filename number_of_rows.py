import pandas as pd

df = pd.read_csv("D:\\New folder\\week 6\\2GB\\en-fr.csv", engine="python")

num_rows = len(df)

print("Number of rows:", num_rows)