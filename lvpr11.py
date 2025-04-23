def main():
    #Declarar variaveis
    stop = True
    positivos = int(0)
    negativos = int(0)
    numero_negativos = int(0)



    #Entrada de dado
    while stop:
        continuar = input()
        if continuar == "n":
            stop = False
        else:
            numero = int(input())
            if numero > 0:
                positivos += numero
            else:
                negativos += numero
                numero_negativos += 1
    print(f"{positivos} {negativos/numero_negativos:.0f}")

if __name__ == '__main__':
    main()