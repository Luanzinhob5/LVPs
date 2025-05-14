def main():
    #Declarar variaveis
    pontuacao = float(0)
    pontuacao_velha = float(0)
    total = float(0)

    #Entrada de dados
    

    #Processos
    for numero in range(5):
        nome = input()
        pontuacao = 0
        for numero in range(10):
            letra = input()
            if letra == "A1":
                pontuacao += 5
            elif letra == "A2":
                pontuacao += 7
            elif letra == "A3":
                pontuacao += 10
            elif letra == "E1":
                pontuacao -= 2
            elif letra == "E2":
                pontuacao -= 5
            elif letra == "E3":
                pontuacao = 0
            if pontuacao < 0:
                pontuacao = 0
        if pontuacao > pontuacao_velha:
            vencedor = pontuacao
            vencedor_nome = nome
        total += pontuacao
        print(f"{nome} {pontuacao:.0f} pontos")
        pontuacao_velha = pontuacao

    print(f"Média de pontos = {total/5:.2f} por jogo")
    print(f"Vencedor {vencedor_nome} com {vencedor} pontos")

        
        
    
if __name__ == '__main__':
    main()