def main():
    #Declarar variaveis
    ano = int(0)
    
    
    #Entrada de dados
    ano = int(input())
   
    
    #Processos
    idade = 2024 - ano
    
    if  idade >= 16 :
        print(f'{idade} anos: PODE VOTAR')
    else:
        print(f'{idade} anos: NÃO PODE VOTAR')

if __name__ == '__main__':
    main()