def main():
    #Declarar variaveis
    a = float(1)
    b = float(2)
    soma = float(0)
    
    #processo do for
    for i in range(10):
        soma += (a + b)/(a + 2)
        a += 1
        b += 1
        

    #saida do for
    print(soma)


if __name__ == '__main__':
    main()