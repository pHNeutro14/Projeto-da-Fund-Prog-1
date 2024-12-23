'''Discentes:   Anderson Lucas, Fabio Oliveira, Tatieny Dayane, Pedro Henrique, Rutemberg de Siqueira'''

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
        while True: #Aqui ele vai entrar em uma repetição para inserir as notas dos alunos
            try:
                nota = float(input("Insira a nota do aluno: - Insira um número negativo para encerrar: \n>"))
                if nota < 0:
                    break
                elif nota >= 0 and nota <= 10: #nesse elif vai permitir que apenas as notas entre 0 e 10 sejam inseridas na lista
                    lista_alunos[nome_aluno].append(nota)
                    print(f"Aluno: {nome_aluno} - Nota: {nota}")
                else: 
                    print("Digite uma nota entre 0 e 10")
            except ValueError: #caso o usuário insira um texto vai entrar nesse except
                print("Insira um número válido")

def exibir_notas(lista_alunos): #nesta função vai exibir as notas, acessando a chave do dicionário que é um aluno e seu atributo que é uma lista de notas
    while True:
        nome_aluno = input("Insira o nome do aluno para exibir a nota ou 0 para encerrar \n>").upper()
        if nome_aluno in lista_alunos:
            nota_aluno = lista_alunos[nome_aluno]
            print(f"Aluno: {nome_aluno} - Notas: {nota_aluno}")
        elif nome_aluno == "0":
            break
        else:
            print("Aluno não encontrado")

def exibir_boletim(lista_alunos): #aqui vai listar o aluno, suas notas e a sua média acompanhado do conceito
    if not lista_alunos:
        print("Não existem alunos cadastrados para exibir boletins.\n")
    else:
        for nome, notas in lista_alunos.items():
            if notas:
                media = sum(notas) / len(notas)
                if media == 0:
                    print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f} - Conceito: E")
                
                elif media >= 1 and media <= 3.5:
                    print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f} - Conceito: D")

                elif media >= 3.6 and media <= 6.0:
                    print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f} - Conceito: C")

                elif media >= 6.1 and media <= 8.5:
                    print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f} - Conceito: B")

                elif media >= 8.6 and media <= 10:
                    print(f"Aluno: {nome} - Notas: {notas} - Média: {media:.2f} - Conceito: A")

            else: # caso não tenha notas ele vai mostrar apenas o nome e informar que não possui notas
                print(f"Aluno: {nome} - Não possui notas cadastradas")

def excluir_alunos(lista_alunos): #nessa função vai excluir o aluno do dicionário
    while True:
        nome_aluno = input("Insira o nome do aluno para excluir - 0 para encerrar \n>").upper()
        if nome_aluno == "0":
            break
        elif nome_aluno not in lista_alunos:
            print("Aluno não encontrado")
        else:
            lista_alunos.pop(nome_aluno)
            print("Aluno Removido")

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
            excluir_alunos(lista_alunos)
        elif escolha == 0:
            break

        else:
            print("\nOpção Inválida, selecione outra opção!\n")

    except ValueError:  # Caso o valor seja diferente do tipo inteiro vai mostrar um print informando a entrada inválida
        print("\nErro: Opção de entrada inválida!!\n")
