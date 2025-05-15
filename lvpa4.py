def main():
    #Declarar variaveis
    a = int(1)
    i = int(0)
    #entrada de dados
    linhas = int(input())

    #processo do for
    for _ in range(linhas):
        print("")
        i +=1
        a = 1
        for _ in range(i):
            print(f"{a}",end="")
            a += 1
    

if __name__ == '__main__':
    main()