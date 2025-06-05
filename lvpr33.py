def main():
    #Declarar variaveis
    game_over = True

    #processo do while
    entrada = input()
    while game_over:
        letra = input()
        if letra.upper() in entrada:
            print("LETRA EXISTENTE, DIGITE OUTRA")
        else:
            print("LETRA INEXISTENTE")
            entrada += letra.upper()
            game_over = False
    print(entrada)
         
             
if __name__ == '__main__':
    main()