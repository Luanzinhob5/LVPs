def main():
    #Declarar variaveis
    estoque_atual = float(0)
    estoque_maxima = float(0)
    estoque_minima = float(0)

    #Entrada de dados
    estoque_atual = float(input())
    estoque_maxima = float(input())
    estoque_minima = float(input())
    
    #Processos e Saida de dados
    quantidade_media = ((estoque_maxima + estoque_minima) /2)

    if estoque_atual >= quantidade_media:
        print(f"NÃO EFETUAR COMPRA")
    else:
        print('EFETUAR COMPRA')
    
      
if __name__ == '__main__':
    main()