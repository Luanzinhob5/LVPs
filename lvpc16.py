def main():
    #Declarar variaveis
    litro = int(0)
    tipo = str(0)

    #Entrada de dados
    litro = int(input())
    tipo = str(input())
    
    #Processos e Saida de dados

    if tipo == 'A':
        valor = 2.9 * litro
        if litro <= 20:
            preco = valor * 0.97
            print(f'{preco:.2f}')
        else:
            preco = valor * 0.95
            print(f'{preco:.2f}')

    else:
        valor = 3.3 * litro
        if litro <= 20:
            preco = valor * 0.96
            print(f'{preco:.2f}')
        
        else:
            preco = valor * 0.94
            print(f'{preco:.2f}')

        
    
        
if __name__ == '__main__':
    main()