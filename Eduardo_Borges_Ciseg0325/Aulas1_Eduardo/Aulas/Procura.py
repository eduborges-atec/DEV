#Algoritmo para Procura
import time
nomproc=""
nomes=["Dario Quental", "Joao Matos", "Liliana Queiroz"]
#Nomes[i][it]

nomproc=("Joao Matos Pereira")
#         0123456789  10

for i in range(len(nomes)):
    print(f"valor e i no for", i )
    for it in range(len(nomes[i])):
        time.sleep(1)
        print(f"valor e it no for interno", it )
        print(nomes[i][it])
        print (nomproc[it])
        if it == (len(nomproc)-1):
            print("tamanho do valor dentro de nomproc")
            break