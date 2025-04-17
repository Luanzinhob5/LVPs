def main():
    #Declarar variaveis
    escolha = int(0)
    n1 = float(0)
    n2 = float(0)
    

    #Entrada de dados
    escolha = int(input())
    if escolha > 6:
        print('OPERACAO INVALIDA')
    else:
        n1 = float(input())
        n2 = float(input())
        raiz = pow(n1,n2)
        
        #Processos e Saida de dados
        if escolha == 1:
            print(f'{n1 + n2}')
        elif escolha == 2:
            print(f'{n1 - n2}')
        elif escolha == 3:
            print(f'{n1*n2}')
        elif escolha == 4:
            print(f'{n1/n2}')
        elif escolha == 5:
            print(f'{n1**n2}')
        elif escolha == 6:
            print(f'{raiz}')

if __name__ == '__main__':
    main()