def main():
    #Declarar variaveis
    pressao = int(0)
    
    #Entrada de dados
    pressao = int(input())

    #Processos
    if pressao < 120:
        print("Pressão normal")
    elif pressao < 130:
        print(f"Elevada")
    elif pressao < 140:
        print(f"Hipertensão estágio 1")
    else:
        print(f"Hipertensão estágio 2")
if __name__ == '__main__':
    main()