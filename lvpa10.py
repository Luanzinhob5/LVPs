def main():
    #Declarar variaveis
    game_over = True
    nota_total = int(0)
    total_alunos = int(0)
    media_geral = int(0)


    #processo do while
    while game_over:
        nome_do_aluno = input()
        if nome_do_aluno == "":
            game_over = False

        else:
            for _ in range(5):
                nota = int(input())
                nota_total += nota

            if nota_total/5 >= 7:
                print(f"{nome_do_aluno}: Média {nota_total/5:.1f}, Aprovado")
            else:
                print(f"{nome_do_aluno}: Média {nota_total/5:.1f}, Reprovado")
            media_geral += nota_total/5
            total_alunos += 1
            nota_total = 0
    print(f"Média geral: {media_geral/total_alunos:.2f}")
                
if __name__ == '__main__':
    main()