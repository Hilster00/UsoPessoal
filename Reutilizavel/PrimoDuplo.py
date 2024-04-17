def primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos_duplos(limite):
    primos_duplos = []
    for i in range(2, limite):
        if eh_primo(i) and eh_primo(i + 2):
            primos_duplos.append((i, i + 2))
    return primos_duplos

# Exemplo de uso:
num = int(input("Digite um número inteiro para verificar se possui um primo duplo: "))
if primo(num):
    primos_duplos = encontrar_primos_duplos(num)
    if primos_duplos:
        print(f"O número primo {num} tem irmãos primos duplos:")
        for primo_duplo in primos_duplos:
            print(primo_duplo)
    else:
        print(f"O número primo {num} não tem irmãos primos duplos.")
else:
    print(f"O número {num} não é primo.")
