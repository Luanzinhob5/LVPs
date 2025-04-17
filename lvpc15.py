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
    if a + b < c or a + c < b or c + b < a:
        print('NÃO É TRIÂNGULO')


    elif a == b == c:
        print('EQUILÁTERO')

    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    
    elif a != b != c:
        print('ESCALENO')
        
    
        
if __name__ == '__main__':
    main()