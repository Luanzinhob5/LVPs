def main():
    #Declarar variaveis
    game_over = True

    #processo do while
    while game_over:
        sexo = input()
        if sexo.upper() in "SN":
            print("RESPOSTA CORRETA") 
            game_over = False
        else:
            print("RESPOSTA INCORRETA, DIGITE S OU N")
             
if __name__ == '__main__':
    main()