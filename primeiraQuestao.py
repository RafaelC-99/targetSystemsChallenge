indice = 13
soma = 0
k = 0

while k < indice:
    print("k antes: " + str(k)) 
    k=k+1
    print("k depois: " + str(k))
    print("soma antes: " + str(soma))
    soma=soma+k
    print("soma depois: " + str(soma))
print(soma)