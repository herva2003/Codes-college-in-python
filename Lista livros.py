print("C A D A S T R O   L I V R O S\n\n> Entrada de Dadosy\n")

quantidade_livros = int(input("Número de livros? "))
print("Dados de", quantidade_livros, "livros")
contador = 0
livros = []
while contador < quantidade_livros:
    codigo_livro = int(input("\tCódigo do livro: "))
    titulo_livro = input("\tTítulo: ")
    preco_lirvo = int(input("\tPreço: "))
    contador = contador + 1

    autores = input('\tAutores: ')
    alls = []
    for i in range(1, int(autores) + 1):
        alls.append(input(f"\tAutor {i}:"))
    livros.append({"Código": codigo_livro, "Título": titulo_livro, "Preço": preco_lirvo, "Autores": alls})

print("\t\t<<< RELATÓRIO >>>\n", "Livros com C superior a R$50,00:\n")
print("Código\t\tTítulo\t\t\tAutores(es)\t\t\tPreço\n"
      "------------------------------------------------------")
contador = 0
for livros in livros:
    if livros["Preço"] > 50:
        print(livros["Código"], livros["Título"], livros["Preço"], livros["Autores"])
