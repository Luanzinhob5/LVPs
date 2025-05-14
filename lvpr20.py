def main():
    #Declarar variaveis
    off = True
    off2 = True
    turma_qtde = int(0)
    turma = str()
    ausentes = int(0)
    presentes = int(0)
    a = int(-1)
    b = float(1)
    maior_ausencia = int(0)
    menor_ausencia = int(100)
    turma_mais_ausente = str()
    turma_menos_ausente = str()
    mais_20_ausencia = int(0)

    #Entrada de dados
    qtde_de_turmas = input()
    while off:
        if b == qtde_de_turmas:
            off = False
        else:
            turma = str(input())
            turma_qtde = int(input())
            b += 1
            a = 0
            ausentes = 0
            presentes = 0
            while off2:
                if a == turma_qtde:
                        off2 = False
                else:
                    matricula = str(input())
                    presenca = str(input())
                    if presenca == "A":
                        ausentes += 1
                    else:
                        presentes += 1
                    a += 1
                ausencia = (100/turma_qtde) * ausentes

                if ausencia > maior_ausencia:
                    maior_ausencia = ausencia
                    turma_mais_ausente = turma

                elif ausencia < menor_ausencia:
                    menor_ausencia = ausencia
                    turma_menos_ausente = turma

                if ausencia >= 20:
                    mais_20_ausencia += 1
                    
            
                print(f"TURMA= {turma} AUSENCIA= {ausencia:.2f} %")
            b += 1
    print(f"TURMA COM MAIOR % DE AUSENCIA= {turma_mais_ausente} AUSENCIA= {maior_ausencia:.2f} %")
    print(f"TURMA COM MENOR % DE AUSENCIA= {turma_menos_ausente} AUSENCIA= {menor_ausencia:.2f}")
    print(f"{mais_20_ausencia} TURMAS COM % DE AUSENCIA SUPERIOR A 20%")
        





if __name__ == "__main__":
    main()