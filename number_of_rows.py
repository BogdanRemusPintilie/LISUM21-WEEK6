import pandas as pd

file_path = 'C:\\Users\\Bogdan\\Desktop\\New folder\\en-fr.csv'
chunk_size = 10000

total_rows = 0
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    total_rows += len(chunk)

print("Total number of rows in the DataFrame:", total_rows)