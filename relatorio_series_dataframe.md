# Relatório: Diferenças entre Series e DataFrame no Pandas

## 1. O que é uma Series?

Uma `pandas.Series` é uma estrutura de dados **unidimensional**, ou seja, representa uma única coluna (ou linha) de dados. Ela possui:
- Um array de valores (de qualquer tipo: int, float, str, etc.)
- Um índice associado a cada valor
- Um único tipo de dado (dtype) para todos os elementos

**Exemplo:**
```python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
```

---

## 2. O que é um DataFrame?

Um `pandas.DataFrame` é uma estrutura de dados **bidimensional**, semelhante a uma tabela (linhas e colunas). Ele possui:
- Múltiplas colunas, cada uma podendo ter um tipo diferente
- Um índice para as linhas
- Um rótulo (nome) para cada coluna

**Exemplo:**
```python
df = pd.DataFrame({"Nome": ["Ana", "Bruno"], "Idade": [22, 35]})
```

---

## 3. Principais Diferenças

| Característica        | Series                          | DataFrame                          |
|-----------------------|---------------------------------|------------------------------------|
| Dimensões             | 1D (uma coluna ou linha)        | 2D (linhas e colunas)              |
| Número de colunas     | Sempre 1                        | Uma ou mais                        |
| Tipos de dados        | Um único dtype                  | Cada coluna pode ter dtype próprio |
| Acesso a dados        | Por índice (`s["a"]`)           | Por coluna e índice (`df["col"]`)  |
| Criação               | A partir de lista, dict, array  | A partir de dict de listas/Series  |
| Relação               | Uma coluna de um DataFrame é uma Series | Um DataFrame é um conjunto de Series |
| Uso típico            | Representar uma variável/atributo | Representar um conjunto de dados completo |

---

## 4. Relação entre os dois

Um DataFrame é, internamente, um **conjunto de Series alinhadas pelo mesmo índice**. Ao selecionar uma única coluna de um DataFrame, o resultado é uma Series:

```python
df["Idade"]  # retorna uma Series
```

E uma Series pode ser convertida em DataFrame:

```python
s.to_frame()  # retorna um DataFrame de uma coluna
```

---

## 5. Conclusão

A Series é ideal para trabalhar com **uma única variável** ou resultado de operações sobre uma coluna. O DataFrame é a estrutura principal para **análise de dados tabulares**, onde múltiplas variáveis são analisadas em conjunto. Na prática, a maioria das operações de análise de dados usa DataFrames, enquanto as Series aparecem como resultado intermediário dessas operações.
