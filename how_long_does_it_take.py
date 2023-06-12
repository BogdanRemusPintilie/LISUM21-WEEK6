import pandas as pd
import dask.dataframe as dd
import modin.pandas as mpd
import time

file_path = 'D:\\New folder\\week 6\\2GB\\en-fr.csv'

start_time = time.time()
df_pandas = pd.read_csv(file_path)
end_time = time.time()
execution_time_pandas = end_time - start_time

start_time = time.time()
df_dask = dd.read_csv(file_path, nrows=100)
end_time = time.time()
execution_time_dask = end_time - start_time

start_time = time.time()
df_modin = mpd.read_csv(file_path)
end_time = time.time()
execution_time_modin = end_time - start_time

print(f"Pandas Execution Time: {execution_time_pandas} seconds")
print(f"Dask Execution Time: {execution_time_dask} seconds")
print(f"Modin Execution Time: {execution_time_modin} seconds")