def main():
    #Declarar variaveis
    salario_fixo = float(0)
    valor_vendas = float(0)

    #Entrada de dados
    salario_fixo = float(input())
    valor_vendas = float(input())
    
    #Processos e Saida de dados
    if valor_vendas <= 1500:
        total = valor_vendas *  0.03
    elif valor_vendas > 1500 :
        total = (valor_vendas - 1500 )* 0.05 + (1500 * 0.03)
    print(total + salario_fixo)
        


        
if __name__ == '__main__':
    main()