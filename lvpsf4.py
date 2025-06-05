def main():
    #Declarar variaveis
    qtde_a = 0

    entrada = input()
    for letra in entrada.upper():
        if letra == "A":
            qtde_a += 1
    
    print(f"A frase tem {qtde_a} letras A")
if __name__ == '__main__':
    main()