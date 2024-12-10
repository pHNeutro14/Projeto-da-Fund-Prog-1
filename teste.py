def adicionar_alunos(lista_alunos):  # função para adicionar os alunos na variável lista_alunos
    while True:
        nome_aluno = input("Insira o nome do aluno - 0 para encerrar e voltar ao menu: \n> ").upper()
        if nome_aluno == "0":
            break
        else:
            lista_alunos[nome_aluno] = []  # Adiciona o aluno no dicionário com uma lista vazia de notas

def exibir_alunos(lista_alunos):  # função para exibir os alunos
    if not lista_alunos:  # caso a lista esteja vazia vai exibir este print abaixo
        print("Não existem alunos cadastrados!!\n")
    else:
        for i in lista_alunos:
            print(i)

def adicionar_notas(lista_alunos):
    nome_aluno = input("Insira o nome do aluno que deseja calcular as notas \n>").upper()
    if nome_aluno not in lista_alunos:
        print("Aluno não encontrado")
    else:
        while True:
            try:
                nota = float(input("Insira a nota do aluno, para encerrar digite um número negativo\n>"))
                if nota >= 0:
                    lista_alunos[nome_aluno].append(nota)
                    print(f"Aluno: {nome_aluno} - Nota: {nota}")
                else:
                    break
            except ValueError:
                print("Insira um número válido")

def exibir_notas(lista_alunos):
    while True:
        nome_aluno = input("Insira o nome do aluno para exibir a nota ou 0 para encerrar \n>").upper()
        if nome_aluno in lista_alunos:
            nota_aluno = lista_alunos[nome_aluno]
            print(f"Aluno: {nome_aluno} - Notas: {nota_aluno}")
        elif nome_aluno == "0":
            break
        else:
            print("Aluno não encontrado")

def exibir_boletim(lista_alunos):
    if not lista_alunos:
        print("Não existem alunos cadastrados para exibir boletins.\n")
    else:
        for nome, notas in lista_alunos.items():
            if notas:
                media = sum(notas) / len(notas)
                print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f}")
            else:
                print(f"Aluno: {nome} - Não possui notas cadastradas")

lista_alunos = {} # Dicionario para exibir e adicionar os alunos acompanhado de suas notas 

while True:  # Menu criado para que o usuário possa interagir mais de uma vez até encerrar
    print("Selecione a opção: ")
    print("1 - Adicionar Alunos")
    print("2 - Exibir Alunos")
    print("3 - Adicionar Notas")
    print("4 - Exibir Notas")
    print("5 - Exibir Boletim")
    print("6 - Excluir Aluno")
    print("0 - Encerrar Programa \n")

    try:  # Caso o usuário use um valor diferente de um tipo inteiro, o try vai garantir que o código não encerre e pedir que o usuário digite novamente
        escolha = int(input("> "))

        if escolha == 1:  # Cada if vai levar para uma função diferente
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
            exibir_notas(lista_alunos)
        elif escolha == 5:
            print("Opção 5 escolhida\n")
            exibir_boletim(lista_alunos)
        elif escolha == 6:
            print("Opção 6 escolhida \n")
        elif escolha == 0:
            break

        else:
            print("\nOpção Inválida, selecione outra opção!\n")

    except ValueError:  # Caso o valor seja diferente do tipo inteiro vai mostrar um print informando a entrada inválida
        print("\nErro: Opção de entrada inválida!!\n")
