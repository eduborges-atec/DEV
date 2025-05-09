import time


# Controlo de listas em 2 dimensoes
cidades=    [  "Lisboa",  "Madrid",  "São Paulo"  ]
#index 1 dimensao 0, 1, 2
#           "Lisboa"
#index 2 dimensao 0 1 2 3 4 5 6
i=0
it=0
while i<=2:
    print ("Valor na 1ª dimensão", cidades[i])
    #numeros[i][?]
    while it< len(cidades[i]):
            print(f"1ª dimensão i = {i}")
            print(f"2ª dimensão it = {it}")
            print("Letra na 2ª dimensão", cidades[i][it])
            time.sleep(1)
            it+=1
    i+=1
