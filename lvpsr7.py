def main():
    #Declarar variaveis
    entrada = str()
    saida = str()

    entrada = input()
    for _ in range(len(entrada)):
        if _ % 2 == 0:
            saida += entrada[_]

    print(saida)

            
if __name__ == '__main__':
    main()