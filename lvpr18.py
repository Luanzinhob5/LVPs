def main():
    #Declarar variaveis
    a = float(37)
    b = float(38)
    c =float(1)
    s = float(0)
    soma = float(0)
    
    #processo do for
    for i in range(36):
        soma += (a * b )/c
        a -= 1
        b -= 1
        c += 1
    #saida do for
    print(soma)

if __name__ == '__main__':
    main()