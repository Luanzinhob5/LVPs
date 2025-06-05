def main():
    #Declarar variaveis
    game_over = True

    #processo do while
    while game_over:
        sexo = input()
        if sexo.upper() in "123456":
            print("OPÇÃO VÁLIDA") 
            game_over = False
        else:
            print("OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6")
             
if __name__ == '__main__':
    main()