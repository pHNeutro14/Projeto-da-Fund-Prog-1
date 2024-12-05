while True:
    print("Selecione a opção: ")
    print("1 - Adicionar Alunos")
    print("2 - Exibir Alunos")
    print("3 - Calcular Notas")
    print("4 - Verificar Notas")
    print("5 - Exibir boletim")
    print("0 - Encerrar Programa \n")

    try:
        escolha = int(input("> "))

        if escolha == 1:
            print("Opção 1 escolhida\n")
        elif escolha == 2:
            print("Opção 2 escolhida\n")
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

    except ValueError:
        print("\nErro: Opção de entrada inválida!!\n")
