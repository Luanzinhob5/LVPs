def main():
    #Declarar variaveis
    n = int(0)
    a = int(0)
    
    #Entrada de dados
    hora = int(input())
    
    #Processos
    if hora >= 9 and hora <= 18:
        print("Dentro do horário comercial")
    else:
        print("Fora do horário comercial")

if __name__ == '__main__':
    main()