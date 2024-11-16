print("-------------| PIZZARIA LOS HERMOSILLOS |--------------\n")
print(">>>>>>>> MENU <<<<<<<<")

def exibirMenu():
    while True:
        try:
            print("\n1 - Cardápio \n2 - Fazer pedido \n3 - Sair \n4 - Adm")
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Valor inválido")

def adm():
    while True:
        try:
            print("1 - Adicionar item \n2 - Remover item \n3 - Histórico \n4 - Sair")
            opcao = int(input("Escolha uma opção: "))            
            return opcao    
        except ValueError:
            print("Valor inválido")

def adicionar_item():
    while True:
        try:
            novo_item = input("Novo item: ").capitalize()
            cardapio[novo_item] = float(input("Preço: "))
            print("\nItem registrado!")
            print(cardapio)
            break
        except ValueError:
            print("Valor inválido")

def remover_item():
    while True:
        try:
            item = input("Item a ser removido: ").capitalize()
            if item in cardapio:
                del cardapio[item]
                print("\nItem removido!")
                print(cardapio)
                break
            else:
                print("Item não encontrado")
        except ValueError:
            print("Valor inválido")

identificador = 0
cardapio = {"Pizza": 20.0, "Hambúrger": 15.5, "Refrigerante": 5.0}
pedidos = []

while True:
    opcao = exibirMenu()
    if opcao == 2:
        while True:
            try:
                identificador += 1
                num = 1
                print("")
                for item in cardapio:
                    print(f"{num} - {item}: {cardapio[item]}")
                    num += 1

                print("\nPedido n°", identificador)
                chaves = list(cardapio.keys()) #lista com as chaves
                ncomida = int(input(f"Item(1 - {num-1}): ")) - 1
                tamanho = len(chaves)

                if ncomida >= 0 and ncomida <= tamanho:
                    comida = chaves[ncomida]
                    if comida in cardapio:
                        unidade = int(input("Quantidade: "))
                        
                        pedido = {"Número de pedido": identificador,"Item": comida, "Quantidade": unidade, "Total": cardapio[comida]*unidade}
                        print(f"\nPedido registrado com sucesso!\n{pedido}\n")
                        pedidos.append(pedido)
                        continuar = input("Outro pedido (s/n)? ")
                        if continuar != "s":
                            print("Pedidos registrados.")
                            break
                    else:
                        print("Item indisponivel")
                        identificador -= 1
                        continue
                else:
                    print("Item indisponivel")
                    break
            except ValueError:
                print("Valor inválido")

    elif opcao == 1:
        print("\n>>>>>>>> CARDÁPIO <<<<<<<<")
        num = 1
        for item in cardapio:
            print(f"{num} - {item}: {cardapio[item]}")
            num += 1
        print("...")

    elif opcao == 4:
        while True:
            print("\nÁREA DO ADMINISTRADOR:")
            opcao = adm()
            if opcao == 1:
                print("\nAdicionar item")
                adicionar_item()
                continue
            elif opcao == 2:
                print("\nRemover item")
                remover_item()
                continue
            elif opcao == 3:
                print("\nHistórico")
                for pedido in pedidos:
                    print(pedido)
                continue
            elif opcao == 4:
                print("...\n")
                break

    elif opcao == 3:
        print("\n...")
        break