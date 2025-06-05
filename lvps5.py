def main():
    #Declarar variaveis
    entrada = str()
    saida = str()
    
    entrada = input()
    a = len(entrada)
    for i in range(len(entrada)):
        saida = entrada[:a]
        a -= 1
        print(saida)
                
if __name__ == '__main__':
    main()