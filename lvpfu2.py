def main():
    #Declarar variaveis
    entrada = int(input())
    entrada2 = int(input())
    entrada3 = int(input())

    def soma(a,b,c):
        s = a + b + c
        print(s)
    
    soma(entrada, entrada2, entrada3)

if __name__ == '__main__':
    main()