def main():
    #Declarar variaveis
    sexo = str(0)
    peso = float(0)
    altura = float(0)
    imc = float(0)


    #Entrada de dados
    sexo = str(input())
    peso = float(input())
    altura = float(input())

    
        
    #Processos e Saida de dados
    imc = peso/(altura**2)

    if sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    elif sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    print(f'PESO IDEAL: {peso_ideal:.2f}')
    print(f'IMC: {imc:.2f}')

    if imc < 17:
        print('MUITO ABAIXO DO PESO')
    elif imc >= 17 and imc <= 18.49:
        print('ABAIXO DO PESO')
    elif imc >= 18.50 and imc <= 24.99:
        print('PESO NORMAL')
    elif imc >= 25 and imc <= 29.99:
        print('ACIMA DO PESO')
    elif imc >= 30 and imc <= 34.99:
        print('OBESIDADE I')
    elif imc > 34.99:
        print('OBESIDADE II (SEVERA)')
        
    


        

if __name__ == '__main__':
    main()