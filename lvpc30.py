def main():
    #Declarar variaveis
    n = int(0)


    #Entrada de dados
    n = int(input())

    
        
    #Processos e Saida de dados
    if n < 999:
        centena = n // 100
        dezena = (n // 10) % 10
        unidade = n % 10
        arm_num = (centena **3) + (dezena**3) + (unidade**3)

    else:
        milhar = n // 1000
        centena = (n // 100) % 10
        dezena = (n // 10) % 10
        unidade = n % 10
        arm_num = (milhar **4) + (centena **4) + (dezena**4) + (unidade**4)

    if n == arm_num:
        print(f"{n} É UM NÚMERO DE ARMSTRONG")
    else:
        print(f"{n} NÃO É UM NÚMERO DE ARMSTRONG")
        


    

    
        
    


        

if __name__ == '__main__':
    main()