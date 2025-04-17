def main():
    #Declarar variaveis
    a = int(0)
    b = int(0)
    
    #Entrada de dados
    a = int(input())
    b = int(input())
    
    #Processos
    if a > b:
        print(f'{a} + {b} = {a+b}')
    else:
        print(f'{a} x {b} = {a*b}')

if __name__ == '__main__':
    main()