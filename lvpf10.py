def main():
    #Declarar variaveis
    temperatura = float(0)
    
    
    #Entrada de dados
    temperatura = float(input())
    

    #Processos
    if temperatura < 0:
        print("Muito frio")
    elif temperatura < 10:
        print(f"Frio")
    elif temperatura < 25:
        print(f"Agradável")
    elif temperatura < 35:
        print(f"Quente")
    else:
        print(f"Muito quente")
if __name__ == '__main__':
    main()