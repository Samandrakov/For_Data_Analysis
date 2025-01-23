import pandas as pd
from name import name

df = pd.read_excel(f'{name}.xlsx')
pre_url_list = df['external_url'].tolist()

with open('urls.txt', 'w', encoding='utf-8') as f:
    f.write('(')
    for i in range(len(pre_url_list)):
        f.write(f"doc.external_url LIKE '{pre_url_list[i]}' OR\n")
