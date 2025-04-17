def main():
    #Declarar variaveis
    a = int(0)
    b = int(0)

    #Entrada de dados
    a = int(input())
    b = int(input())
    
    #Processos e Saida de dados
    if a >= b:
        hora = (24 - a) + b
    else:
        hora = b - a
    print(hora)

        
    
        
if __name__ == '__main__':
    main()