import pandas as pd
from name import name

df_export = pd.read_excel(f"{name}.xlsx")
df_nerc = pd.read_csv("sqllab_untitled_query_1_20240430T150311.csv")

#merged_data = df_export[df_export['external_url'].isin(df_nerc['external_url'])]
merged_data = pd.merge(df_export, df_nerc[['title', 'value']], on="title", how="left")

merged_data.to_excel(f"merged_data.xlsx", index=False)