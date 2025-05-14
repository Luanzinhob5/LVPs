def main():
    #Declarar variaveis
    numero = int(0)
    x = int(1)
    #Entrada de dados
    numero = int(input())
    #Processos
    for n in range(10):
        print(f"{x} x {numero} {x* numero}")
        x += 1

        
if __name__ == '__main__':
    main()