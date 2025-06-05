def main():
    #Declarar variaveis
    qtde_a = 0

    entrada = input()
    for letra in entrada.upper():
        if letra in "AEIOU":
            qtde_a += 1
    
    print(f"A frase tem {qtde_a} vogais")
if __name__ == '__main__':
    main()