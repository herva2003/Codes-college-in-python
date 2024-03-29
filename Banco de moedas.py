banco = {}


def adicionar_moeda():
    while True:
        try:
            index = int(input(">>>> Quantas moedas serão adicionadas? "))
            cont = 0
            while cont < index:
                codigo = int(input("\n>>>> Digite o código da moeda: "))
                if codigo in banco.keys():
                    print("O código dessa moeda já existe, digite outro codigo")
                else:
                    pais = input(">>>> Digite o país de origem da moeda: ")
                    ano = int(input(">>>> Digite o ano de fabricação da moeda: "))
                    moeda = input(">>>> Coloque o tipo da moeda: ")
                    valorm = int(input(">>>> Digite o valor de mercado da moeda: "))
                    valorf = float(input(">>>> Digite o valor da face da moeda:  "))
                    moeda_dados = (pais, ano, moeda, valorm, valorf)
                    dados = banco.fromkeys([codigo], moeda_dados)
                    banco.update(dados)
                    cont += 1
                    print("\n<<<< A moeda foi adicionada com sucesso >>>>")
            break
        except:
            print("<<<< Digite apenas números >>>>")


def imprimir_todas_moedas():
    print('''
    PAIS       ANO      MOEDA    PREÇO DE VENDA    PREÇO DA MOEDA ''')
    for coin in banco:
        print('''        {}     {}     {}        {}             {}'''
              .format(banco[coin][0], banco[coin][1], banco[coin][2], banco[coin][3], banco[coin][4]))


def consultar_dados():
    while True:
        try:
            cod = int(input(">>>> Digite o código da moeda que você deseja buscar: "))
            if cod in banco.keys():
                print('''    --------------------------------
    | - Codigo da moeda   ->   {}
    | - Pais de origem    ->   {} 
    | - Ano de fabricação ->   {}   
    | - Tipo da moeda     ->   {}   
    | - Valor no mercado  ->   R${}   
    | - Valor da moeda    ->   {}
    --------------------------------
          '''.format(cod, banco[cod][0], banco[cod][1], banco[cod][2], banco[cod][3], banco[cod][4]))

            else:
                print("<<<< Esta moeda ainda não está registrada >>>>")
                break
        except:
            print("<<<< O código deve ser apenas números >>>>")


def imprimir_moedas_valor():
    while True:
        try:
            preco = int(input(">>>> Qual o valor das moedas que você deseja buscar? "))
            print('''
    CODIGO     PAIS       ANO      MOEDA    PREÇO DE VENDA    PREÇO DA MOEDA ''')
            for cod, dados in banco.items():
                while True:
                    if preco == dados[3]:
                        print('''       {}   {}     {}     {}        {}             {}'''
                              .format(cod, dados[0], dados[1], dados[2], dados[3], dados[4]))
                        break
                    else:
                        break
            break
        except:
            print("<<<< O preço deve ser apenas números >>>>")


def programa():
    while True:
        print(''' 
    -----------------------------------------------------------
    |  1 - Consultar os dados de uma moeda                    |
    |  2 - incluir uma nova moeda no banco                    |
    |  3 - imprimir todas as moedas com um determinado valor  |
    |  4 - imprimir todas as moedas                           |
    |  0 - Sair do programa                                   |
    -----------------------------------------------------------\n''')
        option = input(">>>> O que você deseja fazer? ")

        if option == "0":
            print(">>>> Fechando o programa...")
            break
        elif option == "1":
            consultar_dados()
        elif option == "2":
            adicionar_moeda()
        elif option == "3":
            imprimir_moedas_valor()
        elif option == "4":
            imprimir_todas_moedas()
        else:
            print(">>>> Escolha inválida")


programa()
