def main():
    #Declarar variaveis
    game_over = True
    contador = int(0)

    #processo do while
    while game_over:
        contador = 0
        entrada = int(input())
        if entrada < 1:
            game_over = False
            

        else:
            for i in range(1, entrada + 1):
                if entrada % i == 0:
                    contador += 1
            print(f"{entrada} TEM {contador - 1} DIVISORES")
            
                
if __name__ == '__main__':
    main()