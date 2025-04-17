def main():
    #Declarar variaveis
    a = int(0)
    b = int(0)
    c = int(0)

    #Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
   
    
    #Processos e Saida de dados
    if  a < b and a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b < c and b < a:
        if c < a:
            print(b, c, a)
        else:
            print(b, a, c)
    elif c < a and c < b:
        if b < a:
            print(c, b, a)
        else:
            print(c, a, b)
    


if __name__ == '__main__':
    main()