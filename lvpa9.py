def main():
    #Declarar variaveis
    nome_do_participante = str()
    pontuacao = int(0)
    media = int(0)
    total_p = int(0)
    game_over = True


    #processo do while
    while game_over:
        pontuacao = 0
        nome_do_participante = input()
        if nome_do_participante == "":
            game_over = False
        else:
            letras_pontuacao = input()
            for letra in letras_pontuacao:
                if letra == "C":
                    pontuacao += 10
                elif letra == "I":
                    pontuacao -=3
                elif letra == "P":
                    pontuacao = 0 
            print(f"{nome_do_participante}: {pontuacao} pontos")
            media += pontuacao
            total_p +=1
    print(f"Média: {media/total_p:.2f} pontos")
                





    

if __name__ == '__main__':
    main()