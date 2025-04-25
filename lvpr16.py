def main():
    #Declarar variaveis
    letra = int(0)
    a = int(0)
    off = True
    media = int(0)

    #Entrada de dados
    
    while off:
        letra = int(input())
        if letra == 0:
            off = False
        else:
            a += 1
            media += letra
            
    print(media / a)


    

if __name__ == '__main__':
    main()