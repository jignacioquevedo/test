import pandas as pd

with open("C:/Users/Chino/Documents/Cursos/Santander Tecnologia/datos_data_engineer.tsv") as tsv_file:
    data = []

    for line in tsv_file:
        data.append(line.split('\t'))

df = pd.DataFrame(data)
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

df.to_csv('C:/Users/Chino/Documents/Cursos/Santander Tecnologia/data_engineer.csv', sep='|', encoding='UTF-8')