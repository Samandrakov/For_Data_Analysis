import pandas as pd
from name import name

df = pd.read_excel(f'{name}.xlsx')
pre_url_list = df['title'].tolist()

with open('title_list.txt', 'w', encoding='utf-8') as f:
    f.write('(')
    for i in range(len(pre_url_list)):
        cleaned_title = str(pre_url_list[i]).replace("'", "")  # Заменяем одинарные кавычки на пустую строку
        f.write(f"doc.title LIKE '{cleaned_title}' OR\n")  # Записываем в файл, обернув строку в одинарные кавычки
