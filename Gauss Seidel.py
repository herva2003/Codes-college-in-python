def print_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def transforme_em_um(matriz, piv, a, coluna):
    if a != 0:
        for j in range(coluna):
            matriz[piv][j] = matriz[piv][j] / a


def transforme_em_zero(matriz, piv, linha, coluna):
    for i in range(linha):
        if i != piv:
            b = matriz[i][piv]
            for j in range(coluna):
                matriz[i][j] = matriz[i][j] - b * matriz[piv][j]


def testando_matriz(matriz, linha, coluna):
    ban = True
    if (linha + 1) == coluna:
        for i in range(linha):
            for j in range(coluna):
                if i == j and matriz[i][j] == 0:
                    ban = False
    else:
        ban = False
    return ban


def gauss_seidel(matriz, linha, coluna, ):
    for i in range(linha):
        for j in range(coluna):
            if i == j:
                a = matriz[i][j]
                transforme_em_um(matriz, i, a, coluna)
                transforme_em_zero(matriz, i, linha, coluna)
                print("\nTransformando as diagonais em 1 e as colunas em 0")
                print_matriz(matriz)


def permuta(linha, perm, perms):
    if not linha:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin] + linha[lin + 1:len(linha)], perm + [linha[lin]], perms)


def permutacoes(linha):
    perms = []
    permuta(linha, [], perms)
    return perms


def acha_primeiro_sem_zero(lista):
    flag = None
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j][j] == 0:
                flag = None
                break
            else:
                flag = i
        if flag is not None:
            break
    return flag


def carrega_matriz(nomearq):
    try:
        arq = open(nomearq, "r")
        qtdlins = int(arq.readline())
        ret = []
        for lin in range(qtdlins):
            texto = arq.readline().split()
            linha = []
            for col in range(qtdlins + 1):
                linha.append(float(texto[col]))
            ret.append(linha)
        arq.close()
        return ret
    except FileNotFoundError:
        print("Arquivo não encontrado")


def resultado():
    try:
        matriz = carrega_matriz('matriz.txt')
        linha = len(matriz)
        coluna = linha + 1

        lista = permutacoes(matriz)
        indice = acha_primeiro_sem_zero(lista)

        print(indice)
        if indice is not None:
            matriz = lista[indice]
            print(matriz)
        else:
            print("Não há como deixar a diagonal principal sem 0")

        print("\nMatriz arrumada")
        print_matriz(matriz)

        result_matriz = testando_matriz(matriz, linha, coluna)
        if result_matriz:
            gauss_seidel(matriz, linha, coluna)
            inicio = 65
            for i in range(linha):
                print(f' {chr(inicio)} = {matriz[i][-1]:.2f}')
                inicio += 1
    except TypeError:
        print("")


resultado()
