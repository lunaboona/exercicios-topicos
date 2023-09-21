import pandas as pd

df = pd.read_csv("votacao_secao_2022_PR.csv", encoding="latin-1")

# filtra candidatos a governador
df = df[df["DS_CARGO"] == "SENADOR"]

# soma a quantidade de votos por município e candidato
df = df.groupby(['NM_MUNICIPIO', 'NM_VOTAVEL'])['QT_VOTOS'].sum().reset_index()

# ordena por município em ordem alfabética e quantidade de votos decrescente
df = df.sort_values(['NM_MUNICIPIO', 'QT_VOTOS'], ascending=[True, False])

for index, row in df.iterrows():
    print(f"{row['NM_MUNICIPIO']} | {row['NM_VOTAVEL']} | {row['QT_VOTOS']}")
