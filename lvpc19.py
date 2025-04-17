def main():
    #Declarar variaveis
    horas = float(0)
    salario_por_hora = float(0)
    salario = float(0)

    #Entrada de dados
    horas = float(input())
    salario_por_hora = float(input())
    
    #Processos e Saida de dados
    if horas/4 <= 40:
        salario = salario_por_hora * horas 
    elif horas/4 > 40:
        salario_sem_extra = salario_por_hora *  160 
        salario_extra = (horas - 160) * (salario_por_hora*1.5)
        salario = salario_sem_extra + salario_extra
    print(f'{salario:.1f}')
        
if __name__ == '__main__':
    main()