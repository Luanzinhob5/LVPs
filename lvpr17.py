def main():
    #Declarar variaveis
    a = float(1)
    b = float(1)
    s = float(0)
    soma = float(0)
    
    #processo do for
    for i in range(50):
        soma = a / b
        s += soma
        a += 2
        b += 1
    #saida do for
    print(s)



    

if __name__ == '__main__':
    main()