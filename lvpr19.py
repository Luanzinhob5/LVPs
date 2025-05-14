def main():
    #Declarar variaveis
    a = float(1)
    b = float(1)
    soma = float(0)
    
    #processo do for
    for i in range(10):
        if i % 2 == 0:
            soma += a / b
        else:
            soma -= a / b
        a += 1
        b = a**2
    #saida do for
    print(soma)


if __name__ == '__main__':
    main()