import json
import csv
import pandas as pd

json_data = r'C:\\Users\\jackb\\Desktop\\FileOpen\\json_data.txt'
csv_write = r'C:\\Users\\jackb\Desktop\\FileOpen\\json_dataFIXED.csv'
main_key = 'people'

# simple (flat) print json
with open(json_data) as json_file:
    data = json.load(json_file)
    for p in data[main_key]:
        print(json.dumps(data, sort_keys=True, indent=4))

df = pd.read_json(json_data)

# if normalization needed
# with open(json_data, 'r') as f:
#     data = json.loads(f.read())
# df_nested_list = pd.json_normalize(data, record_path=[main_key])
# print(df_nested_list)
# print(df_nested_list.info())
# df_nested_list.to_csv(csv_write)

print(df)
print(df.info())
df.to_csv(csv_write)
