def main():
    #Declarar variaveis
    stop = True
    total = float(0)
    a = float(0)


    #Entrada de dado
    while stop:
        continuar = input()
        if continuar == "n":
            stop = False
        else:
            numero = int(input())
            total += numero
            a += 1
    print(total/a)

if __name__ == '__main__':
    main()