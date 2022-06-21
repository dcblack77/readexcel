import pandas

df = pandas.read_excel("Libro.xlsx")
title = df.columns[0]
column = df.columns[1]
print(column)
print("-" * len(column))

for index, row in df.iterrows():
  print(row[title], "||", row[column])
