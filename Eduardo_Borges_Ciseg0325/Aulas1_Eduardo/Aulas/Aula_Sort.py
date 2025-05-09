import time
numeros=[4,3,6,2,1,0]

i=0
numaux=0
troca= True

while troca:

    print(f"variavel{i} Lista de numeros {numeros}")
    time.sleep(1)
    troca=False
    i=0
    while i <= 4:
        if ( numeros [i] > numeros[i+1] ):
            troca=True
            numeros[i], numeros[i+1] = numeros[i+1], numeros[i]

        print(f"variavel{i}")
        time.sleep(1)
        i+=1

print (numeros)