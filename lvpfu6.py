def main():
    #Declarar variaveis
    n = 0
    end = True
    
    #funcao fatorial
    def fatorial(n):
        n_fatorial = 1
        numero = 0
        if n == 0:
            return n_fatorial
        elif n > 0:
            for _ in range(n):
                numero += 1
                n_fatorial *= numero
            return n_fatorial

            
    while end:
        n = int(input())     
        if n < 0:
            end = False
        else:
            print(f"Fatorial({n})={fatorial(n)}")    

if __name__ == '__main__':
    main()