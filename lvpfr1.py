def main():
    #Declarar variaveis
    game_over = True
    maior_numero = int(-50)

    #processo do while
    while game_over:
        entrada = int(input())
        if entrada == 0:
            game_over = False

        else:
            if entrada > maior_numero:
                maior_numero = entrada
    print(maior_numero)
                
if __name__ == '__main__':
    main()