# Demontração de matrizes em python...
TABUADA = []

for  x in range(1,10):
    LINHAS = []
    for y in range (1,10):
        LINHAS.append(x*y)
    TABUADA.append(LINHAS)

    for TABELA in TABUADA:
         print(TABELA)
        
