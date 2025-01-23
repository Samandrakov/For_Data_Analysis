import pandas as pd

df = pd.read_csv("sqllab_untitled_query_4_20240812T150321.csv")

# print(df['name'])
names = df['name'].tolist()
# print(names)

result_list = []

for i in names:
    j = i.split()
    if len(j) < 2:
        print(f"{i}, false name")
        pass
    elif len(j) >2 or len(j) == 2:
        result_list.append(i)
print(result_list)