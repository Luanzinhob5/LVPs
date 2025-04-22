def main():
    #Declarar variaveis
    n1 = int(0)
    a = int(0)
    soma = int(0)
    #Entrada de dado

    #Processos
    while a < 5 :
        n = int(input())
        soma += n
        a += 1
    print(f"{soma/5:.0f}")
    

if __name__ == '__main__':
    main()