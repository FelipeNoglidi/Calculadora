import math

while True:
    print("\nEscolha a operação matemática.\n")
    print("0 - Adição")
    print("1 - Subtração")
    print("2 - Multiplicação")
    print("3 - Divisão")
    print("4 - Módulo")
    print("5 - Elevar à Potência")
    print("6 - Raiz Quadrada")
    print("7 - Logaritmo")
    print("8 - Seno")
    print("9 - Cosseno")
    print("10 - Tangente\n")
    oper = input("Sua opção de menu: ")

    if oper == "0":
        val1 = float(input("\nPrimeiro valor: "))
        val2 = float(input("Segundo valor: "))
        print("\nO resultado é: " + str(val1 + val2) + "\n")
    elif oper == "1":
        val1 = float(input("\nPrimeiro valor: "))
        val2 = float(input("Segundo valor: "))
        print("\nO resultado é: " + str(val1 - val2) + "\n")
    elif oper == "2":
        val1 = float(input("\nPrimeiro valor: "))
        val2 = float(input("Segundo valor: "))
        print("\nO resultado é: " + str(val1 * val2) + "\n")
    elif oper == "3":
        val1 = float(input("\nPrimeiro valor: "))
        val2 = float(input("Segundo valor: "))
        print("\nO resultado é: " + str(val1 / val2) + "\n")
    elif oper == "4":
        val1 = float(input("\nPrimeiro valor: "))
        val2 = float(input("Segundo valor: "))
        print("\nO resultado é: " + str(val1 % val2) + "\n")
    elif oper == "5":
        val1 = float(input("\nBase: "))
        val2 = float(input("Expoente: "))
        print("\nO resultado é: " + str(math.pow(val1, val2)) + "\n")
    elif oper == "6":
        val1 = float(input("\nInforme o valor: "))
        print("\nO resultado é: " + str(math.sqrt(val1)) + "\n")
    elif oper == "7":
        val1 = float(input("\nInforme o valor: "))
        print("\nO resultado é: " + str(math.log(val1, 2)) + "\n")
    elif oper == "8":
        val1 = float(input("\nInforme o valor (em graus) para calcular o seno: "))
        print("\nO resultado é: " + str(math.sin(math.radians(val1))) + "\n")
    elif oper == "9":
        val1 = float(input("\nInforme o valor (em graus) para calcular o cosseno: "))
        print("\nO resultado é: " + str(math.cos(math.radians(val1))) + "\n")
    elif oper == "10":
        val1 = float(input("\nInforme o valor (em graus) para calcular a tangente: "))
        print("\nO resultado é: " + str(math.tan(math.radians(val1))) + "\n")
    else:
        print("\nOpção inválida!")
        continue

    voltar = input("Voltar ao menu principal? (s/n)\n")
    if voltar != 's':
        break