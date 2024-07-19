import pandas as pd
import re
from name import name


def find_context(text, target_words, authors):
    context = []

    text = str(text).replace(",", "").replace(".", "")
    unique_contexts = set()
    i = 0
    for word in target_words:

        if word in authors:
            # Если слово является автором, ничего не делаем с контекстом
            context.append('')
        else:
            # Иначе ищем контекст для слова
            pattern = re.compile(r'(\S+\s+){0,6}' + re.escape(word) + r'(\s+\S+){0,6}')
            matches = re.finditer(pattern, text)

            for match in matches:
                context_str = match.group(0)
                if context_str not in unique_contexts:
                    i += 1
                    unique_contexts.add(context_str)
                    context.append(f"{i}) {match.group(0)}")
                    if i == len(target_words):  # Если достигнуто максимальное количество контекстов
                        break  # Прерываем цикл
    return ', '.join(context)




# Загрузка данных из файла Excel
df = pd.read_excel("merged_data.xlsx")

# Убираем дубликаты из списка значений
df['value'] = df['value'].apply(lambda x: ', '.join(set(x.split(', '))) if isinstance(x, str) else '')

# Добавление столбца для контекста
df["context"] = df.apply(lambda row: find_context(row["document_content"], row["value"].split(", ") if isinstance(row["value"], str) else [], row["publication_author"].split(", ") if isinstance(row["publication_author"], str) else []) if isinstance(row["value"], str) else "", axis=1)

# Сохранение обновленного DataFrame в файл Excel
df.to_excel(f"{name} nerc_context.xlsx", index=False)

