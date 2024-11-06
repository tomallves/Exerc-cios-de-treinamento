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
            
            return print(f"\nSaudações {nome} \nParabéns pelos {idade} de vida! \nVamos interagir! ")
        except ValueError:
            print("Valor inválido")

def par():
    while True:
        try:
            n = int(input("\nDigite um número inteiro: "))
            if n % 2 == 0:
                return print(f"{n} é um número Par")
            else:
                return print(f"{n} é um número Ímpar")
        except ValueError:
            print("Valor inválido")

def maior():
    while True:
        try:
            x = int(input("\nDigite um número inteiro: "))
            y = int(input("Digite outro número inteiro: "))

            if x > y:
                return print(f"{x} é maior que {y}")
            else:
                return print(f"{y} é maior que {x}")
        except ValueError:
            print("Valor inválido")

def letras():
    while True:
        try:
            letra = input("\nEscolha uma letra: ")
            if letra.isalpha() and len(letra) == 1:
                lista = ["a", "e", "i", "o", "u"]
                if letra.lower() in lista:
                    return print(f"{letra} é uma vogal")
                else:
                    return print(f"{letra} é uma concoante")
            else:
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")
            
def menor():
    while True:
        try:
            print("\nEscolha três números")
            x = int(input(": "))
            y = int(input(": "))
            z = int(input(": "))

            if x < y and x < z:
                return print(f"{x} é o menor")
            
            elif y < x and y < z:
                return print(f"{y} o menor")
            else:
                return print(f"{z} é o menor")

        except ValueError:
            print("Valor inválido")

def mes():
    while True:
        try:
            n = int(input("\nEscolha um número (1 - 12): "))

            lista = [" ", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

            if n > 0 and n <= 12:
                return print(f"Este é o mês de {lista[n]}")
            else:
                return print("Valor inválido")
        
        except ValueError:
            print("Valor inválido")

def faixa_etarea():
    while True:
        try:
            idade = int(input("\nDigite uma idade e descubra a faixa étaria: "))
            if idade > 0:
                if idade >= 0 and idade <= 2:
                    return print("Bebê")
                elif idade > 2 and idade <= 12:
                    return print("Criança")
                elif idade > 12 and idade <= 19:
                    return print("Adolescente")
                elif idade > 19 and idade <= 59:
                    return print("Adulto")
                else:
                    return print("Idoso")
            else:
                print("Valor inválido")

        except ValueError:
            print("Valor inválido")

saudacao()

while True:
    try:
        opcao = int(input("\nEscolha uma opção (1 - 6): "))
        print("[0 - para sair]")
        if opcao == 1:
            par()
        elif opcao == 2:
            maior()
        elif opcao == 3:
            letras()
        elif opcao == 4:
            menor()
        elif opcao == 5:
            mes()
        elif opcao == 6:
            faixa_etarea()
        elif opcao == 0:
            print("Até mais!")
            break
        else:
            print("Opção inválida")
    except ValueError:
            print("Valor inválido")