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
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
        
    
        
if __name__ == '__main__':
    main()