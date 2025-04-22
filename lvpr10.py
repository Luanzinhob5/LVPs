def main():
    #Declarar variaveis
    a = int(0)
    somap = int(0)
    soman = int(0)
    nnega = int(0)
    #Entrada de dado

    #Processos
    while a < 5 :
        n = int(input())
        if n > 0:
            somap += n
        else:
            soman += n
            nnega += 1
        a += 1
    print(somap,soman/nnega)
        
    

if __name__ == '__main__':
    main()