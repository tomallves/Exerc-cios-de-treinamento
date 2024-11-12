print("-------------------------------------")
print("Bem vindo!\nMe chamo C3PO, estou ao seu dispor")
print("-------------------------------------")

def saudacao():
    while True:
        try:
            nome = str(input("\nQual o seu nome: "))
            if not nome.isalpha(): 
                print("Nome inválido. Digite apenas letras.")
                continue
            idade = int(input("Sua idade: "))
            
            return print(f"\nSaudações {nome} \nVamos interagir! ")
        except ValueError:
            print("Valor inválido")

def soma():
    while True:
        try:
            print(f"\nDescubra a soma dos valores entre dois números inteiros")

            inicio = int(input("Nº 1: "))
            fim = int(input("Nº 2: "))

            resultado = 0
            if inicio > fim:
                for i in range(fim, inicio + 1):
                    resultado = resultado + i
                print(f"({inicio} - {fim}) = {resultado}")
            else:
                for i in range(inicio, fim + 1):
                    resultado = resultado + i
                print(f"({inicio} - {fim}) = {resultado}")
            break
        except ValueError:
            print("Valor inválido")

def fatorial():
    while True:
        try:
            x = int(input("\nDigite um número: "))
            fator = 1
            for i in range(1, x+1):
                fator *= i
            print(f"O fatorial de {x} é: {fator}")
            break
        except ValueError:
            print("Valor inválido")

def primos():
    while True:
        try:
            print("\nDescubra um número primo")
            n = int(input("Digite um número: "))
            if n > 2:
                for i in range(2, n):
                    if (n % i) == 0:
                        return print(f"{n} não é primo")
                        break
                    else:
                        return print(f"{n} é primo")
                        break
            else:
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")

def calculadora():
    while True:
        try:
            print("\nCalculadora")
            x = float(input(":"))
            if x == 00:
                break
            operacao = input("(+|-|*|/): ")
            if operacao == "00":
                break
            y = float(input(": "))
            if y == 00:
                break

            if operacao == "+":
                print(f"{x} {operacao} {y} = {x + y}")
            elif operacao == "-":
                print(f"{x} {operacao} {y} = {x - y}")
            elif operacao == "*":
                print(f"{x} {operacao} {y} = {x * y}")
            elif operacao == "%" or operacao == "/":
                print(f"{x} {operacao} {y} = {x / y}")
            else:
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")

saudacao()

while True:
    try:
        opcao = int(input("\nEscolha uma opção (0 - 4) \n[0 - para sair]: "))
        if opcao == 1:
            soma()
        elif opcao == 2:
            fatorial()
        elif opcao == 3:
            primos()
        elif opcao == 4:
            calculadora()
        elif opcao == 0:
            print("Até mais!")
            break
        else:
            print("Opção inválida")
    except ValueError:
            print("Valor inválido")