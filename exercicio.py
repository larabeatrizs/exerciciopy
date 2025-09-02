#exercicio 1
# numeros = [1 ,2 ,3]
# numeros.append([4, 5])
# print(numeros)
#a saida será  [1, 2, 3, [4, 5]]

 #exercicio 2 
 #dará erro pois o elemento nao existe

 #exercicio 3
 #a diferença é que lista é mutavel e tupla é imutavel

 #exercicio 4
# tupla = (10 ,20, 30)
# print(tupla[1])
# #seria impresso 20 

#exercicio 5
# notas = {
#     "Ana": 8.5,
#     "Bruno": 6.0,
#     "Carlos": 9.0
# }
# #colocando print(notas["Bruno"])

#exercicio 6

# Estados = {
#     "RS": ["Gravatai", "Pelotas", "Erechim"],
#     "SC": ["Joinville", "Jaragua", "Blumenau"],
#     "Estado3": ["Curitiba", "Toledo", "Maringa"]
# }

#exercicio 7
#print(Estados["SC"] [0])

#excercicio 8
# nomes_lista = []

# for i in range(5):
#     nome = input(f"Digite o {i+1}º nome: ")
#     nomes_lista.append(nome)

# print("\nLista de nomes:", nomes_lista)


# nomes_tupla = tuple(nomes_lista)


# print("Tupla de nomes:", nomes_tupla)

#exercicio 9

nomes = []
while True:
   
    print("\n--- MENU ---")
    print("1  Adicionar nomes")
    print("2  Remover nome")
    print("3  Alterar nome")
    print("4  Mostrar lista de nomes")
    print("5  Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome para adicionar: ")
        nomes.append(nome)
        print(f" Nome '{nome}' adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome que deseja remover: ")
        if nome in nomes:
            nomes.remove(nome)
            print(f" Nome '{nome}' removido com sucesso!")
        else:
            print(" Nome não encontrado na lista.")

    elif opcao == "3":
        nome_antigo = input("Digite o nome que deseja alterar: ")
        if nome_antigo in nomes:
            novo_nome = input("Digite o novo nome: ")
            indice = nomes.index(nome_antigo)
            nomes[indice] = novo_nome
            print(f" Nome '{nome_antigo}' alterado para '{novo_nome}'.")
        else:
            print(" Nome não encontrado na lista.")

    elif opcao == "4":
        if nomes:
            print("\n Lista de nomes:")
            for i, nome in enumerate(nomes, start=1):
                print(f"{i}. {nome}")
        else:
            print("⚠ A lista está vazia.")

    elif opcao == "5":
        print(" Saindo do programa...")
        break

    else:
        print(" Opção inválida! Tente novamente.")

