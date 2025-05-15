def main():
    #Declarar variaveis
    i = int(0)
    a = int(0)

    #entrada de dados
    entrada = int(input())
    #processo do for
    for i in range(entrada):
        a += 1
        #saida do for
        print("A"*a)

if __name__ == '__main__':
    main()