def main():
    #Declarar variaveis
    qtde_de_turmas = str()
    turma = str()
    qtde_alunos = int(0)
    matricula = str()
    frequencia = str()
    contagem = int(0)
    contagem_2 = int(0)
    ausencia_turma = float(0)
    maior_ausencia = float(0)
    menor_ausencia = float(100)
    ausencia = float(0)
    turma_ausencia_superior_a_20 = int(0)
    turma_menor = str()
    turma_maior = str()


    #Entrada da qtde geralde turmas
    qtde_de_turmas = int(input())
    while contagem != qtde_de_turmas:
        #Entrada da turma e qtde de alunos nela
        turma = input()
        qtde_alunos = int(input())
        contagem += 1
        contagem_2 = 0
        ausencia_turma = 0
        while contagem_2 != qtde_alunos:
            #Entrada de matricula e frequencia do aluno
            matricula = input()
            frequencia = input()
            contagem_2 += 1
            if frequencia == "A":
                ausencia_turma +=1

        #Porcentagem de ausencia da turma
        if ausencia_turma == 0:
            ausencia = 0
        else:
            ausencia = (ausencia_turma/qtde_alunos) * 100

        #Turmas com mais de 20% de AUSENCIA
        if ausencia > 20:
            turma_ausencia_superior_a_20 += 1
        
        #Maior e menor AUSENCIA
        if maior_ausencia < ausencia:
            maior_ausencia = ausencia
            turma_maior = turma
        elif menor_ausencia > ausencia:
            menor_ausencia = ausencia
            turma_menor = turma

        #Saída da ausencia da turma
        print(f"TURMA= {turma} AUSENCIA= {ausencia:.2f} %")

    #Saida de turma com maior e menor ausencia e turma com ausencia superior a 20
    print(f"TURMA COM MAIOR % DE AUSENCIA= {turma_maior} AUSENCIA= {maior_ausencia:.2f}%")
    print(f"TURMA COM MENOR % DE AUSENCIA= {turma_menor} AUSENCIA= {menor_ausencia:.2f}%")
    print(f"{turma_ausencia_superior_a_20:.0f} TURMAS COM % DE AUSENCIA SUPERIOR A 20%")
    


if __name__ == "__main__":
    main()