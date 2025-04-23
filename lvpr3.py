def main():
    #Declarar variaveis
    stop = True
    total = int(0)


    #Entrada de dado
    while stop:
        continuar = input()
        
        if continuar == "n":
            stop = False
        else:
            numero = int(input())
            total += numero
    print(total)

if __name__ == '__main__':
    main()