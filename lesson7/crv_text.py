# import csv
# https://alexanderdyakonov.files.wordpress.com/2015/04/ama2015_pandas.pdf
# https://proglib.io/p/pandas-tricks/

'''
функция csv.reader
функция csv.writer
класс csv.Dictwriter
класс csv.DictReader
'''


# csv.writer
# car_data = [['brand', 'price', 'year'], ['Volvo', 1.5, 2017], ['Lada', 0.5, 2018], ['Audi', 2.0, 2018]]
#
# with open('example.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';') #
#     writer.writerows(car_data)
# print('Writing complete!')
# exit()
# csv.reader
#
# with open('example.csv') as f:
#     reader = csv.reader(f, delimiter=';')
#     for row in reader:
#         print(row)
# exit()
# csv.Dictwriter
# data_dict = [{'Name': 'Dima', 'age': 28},
#              {'age': 29, 'Name': 'Kate'},
#              {'Name': 'Mike', 'age': 31}]
#
# fieldnames = ['Name', 'age']
#
# with open('example_1.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter='&', fieldnames=fieldnames)
#     writer.writeheader()
#     for i in range(len(data_dict)):
#         writer.writerow(data_dict[i])
# exit('Stop Drive')
# csv.Dictreder

# with open('example_1.csv') as f:
#     reader = csv.DictReader(f, delimiter='&')
#     for row in reader:
#         print(dict(row))
#
# exit('Ho-ho-ho, dirk')

import pandas as pd

DataFrame_from_csv = pd.read_csv('example.csv', sep='&')
print(type(DataFrame_from_csv))
print(DataFrame_from_csv)
