def main():
    #Declarar variaveis
    n1 = float(0)
    n2 = float(0)
    n3 = float(0)
    n4 = float(0)

    #Entrada de dados
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    
        
    #Processos e Saida de dados
    if n1 > n2 and n1 > n3 and n1 > n4:
        a = n1
    elif n2 > n3 and n2 > n4:
        a = n2
    elif n3 > n4:
        a = n3
    else:
        a = n4
    
    if n1 < n2 and n1 < n3 and n1 < n4:
        b = n1
    elif n2 < n3 and n2 < n4:
        b = n2
    elif n3 < n4:
        b = n3
    else:
        b = n4
        
    print(a + b)
        

if __name__ == '__main__':
    main()