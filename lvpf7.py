def main():
    #Declarar variaveis
    salario = float(0)
    
    #Entrada de dados
    salario = float(input())

    #Processos
    if salario < 1903.99:
        print("Isento")
    elif salario < 2826.66:
        print(f"Imposto: R$ {salario*0.075:.2f}")
    elif salario < 3751.06:
        print(f"Imposto: R$ {salario*0.15:.2f}")
    elif salario < 4664.69:
        print(f"Imposto: R$ {salario*0.225:.2f}")
    else:
        print(f"Imposto: R$ {salario*0.275:.2f}")
if __name__ == '__main__':
    main()