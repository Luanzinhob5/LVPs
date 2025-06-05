def main():
    #Declarar variaveis
    game_over = True
    game_over2 = True
    contador = int(0)

    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a

    #processo do while
    while game_over:
        entrada = int(input())
        if entrada < 1:
            game_over = False
            
        else:
            entrada2 = int(input())
            print(f"MDC({entrada},{entrada2})={mdc(entrada,entrada2)}")

            
            
                
if __name__ == '__main__':
    main()