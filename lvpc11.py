def main():
    #Declarar variaveis
    a = float(0)
    b = float(0)
    c = float(0)
    #Entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())
   
    
    #Processos e Saida de dados
    if  a < b and a < c:
        print(b+c)
    elif b < c :
        print(a+c)
    else:
        print(a+b)
    


if __name__ == '__main__':
    main()