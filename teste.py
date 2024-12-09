def adicionar_alunos(lista_alunos): #função para adicionar os alunos na variavel lista_alunos
    while True: 
        nome_aluno = input("Insira o nome do aluno - 0 para encerrar e voltar ao menu: \n> ")
        if nome_aluno == "0":
            break
        else:
            lista_alunos[nome_aluno] = [] #Adiciona o aluno no dicionário com uma lista vazia de notas

def exibir_alunos(lista_alunos): #função para exibir os alunos
    if not lista_alunos: # caso a lista esteja vazia vai exibir este print abaixo
        print("Não existe alunos cadastrados!!\n")
    else: 
        for i in lista_alunos:
            print(i)

def adicionar_notas(lista_alunos):
    nome = input("Insira o nome do aluno que deseja calcular as notas \n>")
    if nome not in lista_alunos:
        print("Aluno não encontrado")
    else:
        while True:
            try:
                nota = float(input("Insira a nota do aluno, para encerrar digite um número negativo\n>"))
                if nota >= 0:
                    lista_alunos[nome].append(nota)
                    print("Esta no caminho certo")
                else:
                    break
            except ValueError:
                print("Insira um número")

def exibir_notas(lista_alunos):
    for nome_aluno, nota_aluno in lista_alunos:
        print(nome_aluno, nota_aluno)

lista_alunos = {} #variável global para exibir e adicionar os alunos

while True: #Menu criado para que o usuário possa interagir mais de uma vez até encerrar
    print("Selecione a opção: ")
    print("1 - Adicionar Alunos")
    print("2 - Exibir Alunos")
    print("3 - Adicionar Notas")
    print("4 - Exibir Notas")
    print("5 - Exibir boletim")
    print("0 - Encerrar Programa \n")

    try: #caso o usuário use um valor diferente de um tipo inteiro, o try vai garantir que o código não encerre e pedir que o usuário digite novamente
        escolha = int(input("> "))

        if escolha == 1: #cada if vai levar para uma função diferente
            print("Opção 1 escolhida\n")
            adicionar_alunos(lista_alunos)
        elif escolha == 2:
            print("Opção 2 escolhida\n")
            exibir_alunos(lista_alunos)
        elif escolha == 3:
            print("Opção 3 escolhida\n")
            adicionar_notas(lista_alunos)
        elif escolha == 4:
            print("Opção 4 escolhida\n")
            exibir_notas()
        elif escolha == 5:
            print("Opção 5 escolhida\n")
        elif escolha == 0:
            break

        else:
            print("\nOpção Inválida, selecione outra opção!\n")

    except ValueError: #caso o valor seja diferente do tipo inteiro vai mostrar um print informando a entrada inválida
        print("\nErro: Opção de entrada inválida!!\n")
