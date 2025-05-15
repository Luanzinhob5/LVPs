def main():
    #Declarar variaveis
    i = int(0)
    a = int(1)
    numero = int(0)
    #entrada de dados
    altura = int(input())
    largura = int(input())
    #processo do for
    for _ in range(altura):
        print("")
        for _ in range(largura):
            numero += 1
            print(f"{numero} ",end="")

if __name__ == '__main__':
    main()