import pandas as pd
from name import *
import csv

def name_extracction(name, format, char):
    if format == 'xlsx':
        df = pd.read_excel(f'{name}.{format}')
    elif format == 'csv':
        df = pd.read_csv(f'{name}.{format}')

    pre_total_list = df[char].tolist()
    total_list = [str(company) for company in pre_total_list]
    return total_list

total_globaldata = name_extracction(name_2, 'xlsx', 'name')
list1 = total_globaldata
print(len(list1))
# print(total_globaldata)
total_companies_market = name_extracction(name_1, 'csv', 'Name')
list2 = total_companies_market
print(len(list2))
# print(total_companies_market)

list1_low = [word.lower() for word in list1]
list2_low = [word.lower() for word in list2]

comp_counter = 0
for word in list1_low:
    if word in list2_low:
        comp_counter += 1
        pass
    else:
        list2_low.append(word)
print(list2_low)
print(f"Количество дублей {comp_counter}")

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name'])
    for word in list2_low:
        writer.writerow([word])
