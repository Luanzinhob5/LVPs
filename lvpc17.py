def main():
    #Declarar variaveis
    a = int(0)
    b = int(0)
    c = int(0)

    #Entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    
    #Processos e Saida de dados
    if a < b and a < c:
        if b < c:
            d = a
            f = b
            g = c
        else:
            d = a
            f = c
            g = b
    elif b < c and b < a:
        if c < a:
            d = b
            f = c
            g = a
        else:
            d = b
            f = a
            g = c
    elif c < a and c < b:
        if b < a:
            d = c
            f = b
            g = a
        else:
            d = c
            f = a
            g = b

    a = d
    b = f
    c = g
    print(f'{a} {b} {c}')


if __name__ == '__main__':
    main()
        