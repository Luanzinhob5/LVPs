def main():
    #Declarar variaveis
    a = int(0)
    b = int(0)
    c = int(0)
    d = int(0)
    
    #Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    #Processos
    media = (a + b + c + d)/4
    if media >= 60:
        print(f'APROVADO com média {media:.2f}')

if __name__ == '__main__':
    main()