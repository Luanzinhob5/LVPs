def main():
    #Declarar variaveis
    stop = True
    total = int(0)
    a = int(0)


    #Entrada de dado
    while stop:
        
        if a == 5:
            stop = False
        else:
            numero = int(input())
            total += numero
            a += 1
    print(total)

if __name__ == '__main__':
    main()