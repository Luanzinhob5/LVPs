def main():
    #Declarar variaveis
    n = 1
    end = True
    
    #funcao quadrado
    def quadrado(n):
        x = n**0.5
        aprox = round(x)**2
        numero_d = round(x) * 2
        quadrado = (n + aprox)/(numero_d) 
        return quadrado


    while end:
        n = int(input())
        if n < 0:
            end = False
        else:
            print(f"N={n:.4f} RAIZ={quadrado(n):.6f}")


if __name__ == '__main__':
    main()