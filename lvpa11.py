def main():
    #Declarar variaveis
    game_over = True
    nota = int(0)
    jogador = str()
    nota_letra = str()
    maior_nota = int(0)
    melhor_jogador = str()

    #processo do while
    while game_over:
        jogador = input()
        game_over = True
        nota = 0
        if jogador == "":
            game_over = False

        else:
            for _ in range(5):
                nota_letra = input()
                if nota_letra == "A":
                    nota += 5
                else:
                    nota -= 2

                if nota < 0:
                    nota = 0

            if nota > maior_nota:
                maior_nota = nota
                melhor_jogador = jogador

            print(f"{jogador}: {nota} pontos")
    print(f"Jogador com maior pontuação: {melhor_jogador} ({maior_nota} pontos)")

                
if __name__ == '__main__':
    main()