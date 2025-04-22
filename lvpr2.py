def main():
    #Declarar variaveis
    n = int(0)
    a = int(0)
    
    #Entrada de dados
    n = int(input())
    
    #Processos
    while a < 10:
        a += 1
        print(f"{a} x {n} = {a*n}")

if __name__ == '__main__':
    main()