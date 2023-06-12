import pandas as pd
import yaml

df = pd.read_csv("D:\\New folder\\week 6\\2GB\\en-fr.csv", nrows=5)

df.columns = df.columns.str.replace('[^\w\s]', '', regex=True)
df.columns = df.columns.str.strip()

with open('magicfile.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

expected_columns = yaml_data['columns']
expected_separator = yaml_data['separator']

if len(df.columns) != len(expected_columns):
    print('Error: Number of columns does not match the YAML file.')

if set(df.columns) != set(expected_columns):
    print('Error: Column names do not match the YAML file.')

if expected_separator != ',':
    print('Error: Separator does not match the YAML file.')

# Assuming you have already performed the necessary validations
output_filename = 'result.txt.gz'
df.to_csv(output_filename, sep=',', compression='gzip', index=False)