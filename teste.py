while True:
    print("Selecione a opção: ")
    print("1 - Calcular Notas")
    print("2 - Verificar Notas")
    print("3 - Exibir boletim")
    print("0 - Encerrar Programa")

    try:
        escolha = int(input("> "))

        if escolha == 1:
            print("Opção 1 escolhida")
        if escolha == 2:
            print("Opção 2 escolhida")
        if escolha == 3:
            print("Opção 3 escolhida")
        if escolha == 0:
            break

    except ValueError:
        print("\nErro: Opção de entrada inválida!!\n")