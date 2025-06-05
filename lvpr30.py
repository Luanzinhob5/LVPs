def main():
    #Declarar variaveis
    game_over = True

    #processo do while
    while game_over:
        sexo = input()
        if sexo.upper() in "MF":
            print("SEXO VÁLIDO") 
            game_over = False
        else:
            print("SEXO INVÁLIDO, DIGITE F OU M")
             
if __name__ == '__main__':
    main()