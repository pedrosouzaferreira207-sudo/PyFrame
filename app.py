import pandas as pd
import string

nomes     = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia"]
idades    = [22, 35, 28, 41, 19, 30, 25, 38, 27, 33]
alturas   = [1.65, 1.78, 1.72, 1.60, 1.85, 1.68, 1.80, 1.63, 1.75, 1.70]
salarios  = [2500, 4800, 3200, 6100, 1800, 3900, 4200, 5500, 2900, 3600]
cidades   = ["BH", "SP", "RJ", "Curitiba", "Salvador", "Fortaleza", "Recife", "Manaus", "Porto Alegre", "Brasília"]

indice = list(string.ascii_uppercase[:10])

df = pd.DataFrame({
    "Nome":    nomes,
    "Idade":   idades,
    "Altura":  alturas,
    "Salario": salarios,
    "Cidade":  cidades
}, index=indice)

print("=== DataFrame completo ===")
print(df)

df["Salario"] = df["Salario"] + 1

print("\n=== 2 primeiras linhas ===")
print(df.head(2))

print("\n=== 4 últimas linhas ===")
print(df.tail(4))

dicionario = df.to_dict()

print("\n=== Dicionário resultante ===")
print(dicionario)
