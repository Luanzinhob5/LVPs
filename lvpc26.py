def main():
    #Declarar variaveis
    idade = float(0)
    peso = float(0)
    

    #Entrada de dados
    idade = int(input())
    peso = int(input())
    
        
    #Processos e Saida de dados
    if idade <= 17:
        print(f'{peso*0.040:.1f} LITROS')
    elif idade >= 18 and idade <= 55:
        print(f'{peso * 0.035:.1f} LITROS')
    elif idade >= 56 and idade <= 65:
        print(f'{peso * 0.03:.1f} LITROS')
    elif idade >= 66:
        print(f'{peso * 0.025:.1f} LITROS')
        

if __name__ == '__main__':
    main()