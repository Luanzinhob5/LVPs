def main():
    #Declarar variaveis
    a = int(0)

    
    #processo do for
    for i in range(1,11):
        a += 1
        for b in range(1,11):
            print(f"{a} x {b} = {a*b}")

        

    #saida do for


if __name__ == '__main__':
    main()