def main():
    #Declarar variaveis
    estoque = int(0)
    entrada = "a"
    nome_do_produto = str("a")
    game_over = True
    game_over2 = True
    #entrada de dados

    #processo do for
    while game_over:
        game_over2 = True
        nome_do_produto = input()
        if nome_do_produto == "":
            game_over = False
        else:
            estoque += int(input())

            while game_over2:
                entrada = input()
                if "V" in entrada:
                    estoque -= int(entrada.replace("V","0"))
                elif "R" in entrada:
                    estoque += int(entrada.replace("R","0"))
                
                elif "C" in entrada:
                    print(f"Estoque atual: {estoque}")
                
                elif "X" in entrada:
                    print(f"Produto: {nome_do_produto},")
                    print(f"Estoque final: {estoque}")
                    game_over2 = False
                
                if estoque < 0:
                    estoque = 0




    

if __name__ == '__main__':
    main()