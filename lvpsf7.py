def main():
    #Declarar variaveis
    o = 0

    for palavra in range(10):
        entrada = input()
        for letra in entrada.upper():
            if letra == "O":
                o += 1
    print(f"Soma das letras O: {o}")
   

if __name__ == '__main__':
    main()