def main():
    #Declarar variaveis
    numero = int(0)
    
    #Entrada de dados
    numero = int(input())

    #Processos
    if numero % 3 == 0 and numero % 5 == 0:
        print("Múltiplo de 3 e 5")
    elif numero % 3 == 0:
        print("Múltiplo de 3")
    elif numero % 5 == 0:
        print("Múltiplo de 5")
    else:
        print("Não é múltiplo de 3 nem de 5")

if __name__ == '__main__':
    main()