def main():
    #Declarar variaveis
    n1 = int(0)
    capicua = int(0)
    
    #Entrada de dados
    n1 = int(input())

        
    #Processos e Saida de dados
    centena = (n1 // 100) %10
    dezena = (n1 // 10) % 10
    unidade = n1 % 10
    milhar =  n1 // 1000
    
    capicua = (unidade * 1000) + (dezena * 100) + (centena * 10) + milhar
    if n1 == capicua:
        print(f'{n1} É UMA CAPICUA')
    else:
        print(f'{n1} NÃO É UMA CAPICUA')



if __name__ == '__main__':
    main()