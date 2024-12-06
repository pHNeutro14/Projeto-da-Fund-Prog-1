def adicionar_alunos(lista_alunos): 
    while True: 
        nome_aluno = input("Insira o nome do aluno - 0 para encerrar e voltar ao menu: \n> ")
        if nome_aluno == "0":
            break
        else:
            lista_alunos.append(nome_aluno)

def exibir_alunos(lista_alunos):
    if not lista_alunos:
        print("Não existe alunos cadastrados!!\n")
    else: 
        for i in lista_alunos:
            print(i)

lista_alunos = [] #variável global para exibir e adicionar os alunos

while True: #Menu criado para que o usuário possa interagir mais de uma vez até encerrar
    print("Selecione a opção: ")
    print("1 - Adicionar Alunos")
    print("2 - Exibir Alunos")
    print("3 - Calcular Notas")
    print("4 - Verificar Notas")
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
        elif escolha == 4:
            print("Opção 4 escolhida\n")
        elif escolha == 5:
            print("Opção 5 escolhida\n")
        elif escolha == 0:
            break

        else:
            print("\nOpção Inválida, selecione outra opção!\n")

    except ValueError: #caso o valor seja diferente do tipo inteiro vai mostrar um print informando a entrada inválida
        print("\nErro: Opção de entrada inválida!!\n")
