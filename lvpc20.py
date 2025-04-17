def main():
    #Declarar variaveis
    a = str(0)
    b = float(0)

    #Entrada de dados
    a = str(input())
    b = float(input())
    
    #Processos e Saida de dados
    if a == 'M':
        peso_ideal = (72.7 * b) - 58
        print(f'{peso_ideal}')

    else:
        peso_ideal = (62.1 * b) - 44.7
        print(f'{peso_ideal}')

        
    
        
if __name__ == '__main__':
    main()