import csv
import pandas as pd

csv_name = r'C:\\Users\\jackb\Desktop\\FileOpen\\biostats.csv'
csv_write = r'C:\\Users\\jackb\Desktop\\FileOpen\\biostatsFIXED.csv'

# print csv
# with open(csv_name, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in csvreader:
#         print(', '.join(row))

# fancy csv reader
# with open(csv_name) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     column_names = []
#     for row in csv_reader:

#         if line_count == 0:
#             column_names.append(row)
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(', '.join(row))
#             line_count += 1
#     print(f'Processed {line_count} lines.')

# parse with pandas
df = pd.read_csv(csv_name)
print(df)

# write to csv with pandas
df = pd.read_csv(csv_name)
df.to_csv(csv_write)
