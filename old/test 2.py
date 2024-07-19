import pandas as pd
from difflib import get_close_matches, SequenceMatcher

df = pd.read_excel('bel.xlsx')
pre_total_list = df['external_url'].tolist()
export_list = [str(url) for url in pre_total_list]
print(f"Export list {export_list}")
print(f"Length {len(export_list)}")

df = pd.read_csv('../nerc.csv')
pre_nerc_list = df['external_url'].tolist()
nerc_list = [str(url) for url in pre_nerc_list]

print(f"Nerc list {nerc_list}")
print(f" Nerc length {len(nerc_list)}")

result_list = []

for j in range(len(export_list)):
   if nerc_list[j] in export_list:
       result_list.append(1)

   else:
       result_list.append(0)

print(result_list)