def main():
    #Declarar variaveis
    primeiro_time = str()
    segundo_time = str()
    qtde_gol_primeiro = float(0)
    qtde_gol_segundo = float(0)
    media_dos_gols = float(0)
    time_mais_gols = str()
    menor_qtde_gols_partida = float(10)
    maior_qtde_gols = float(0)
    total_gols = float(0)
    i = int(0)
    stop = True

    while stop:
        #Entrada dos time 1 e 2
        primeiro_time = input()
        segundo_time = input()

        #Processo de parada do while
        if primeiro_time == "":
            stop = False
        else:
            #entrada gols do time 1 e 2
            qtde_gol_primeiro = int(input())
            qtde_gol_segundo = int(input())

            print(f"{primeiro_time} X {segundo_time}")

            #Saida do vencedor/empate
            if qtde_gol_primeiro > qtde_gol_segundo:
                print(f"Vencedor: {primeiro_time}")
            elif qtde_gol_primeiro < qtde_gol_segundo:
                print(f"Vencedor: {segundo_time}")
            else:
                print(f"Empate")
            
            #Processo de menor gols em uma partida
            if menor_qtde_gols_partida > qtde_gol_primeiro :
                menor_qtde_gols_partida = qtde_gol_primeiro
            elif menor_qtde_gols_partida > qtde_gol_segundo:
                menor_qtde_gols_partida = qtde_gol_segundo

            #Processo de time que mais fez gols
            if qtde_gol_primeiro > maior_qtde_gols:
                maior_qtde_gols = qtde_gol_primeiro
                time_mais_gols = primeiro_time
            elif qtde_gol_segundo > maior_qtde_gols:
                maior_qtde_gols = qtde_gol_segundo
                time_mais_gols = segundo_time
            #Processo de media dos gols
            total_gols += qtde_gol_primeiro + qtde_gol_segundo
            i += 1
    
    media_dos_gols = total_gols/ i
    #Saida da media de gols, time que mais fez gols, menor numero de gols em uma partida
    print(f"Média de Gols: {media_dos_gols:.2f} por jogo")
    print(f"Time que fez mais gols em um jogo: {time_mais_gols}")
    print(f"Menor número de gols em uma partida: {menor_qtde_gols_partida}")
            

            


 
if __name__ == '__main__':
    main()