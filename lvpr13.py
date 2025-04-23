def main():
    #Declarar variaveis
    a = float(0)
    maior = float(0)
    menor = float(200)
    mulheres = float(0)
    alturaf = float(0)
    qtde_homens = float(0)
    #Entrada de dado

    #Processos
    while a < 5 :
        sexo = str(input())
        n = float(input())
        if sexo == "f":
            alturaf += n
            mulheres += 1
        else :
            qtde_homens += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        a += 1
    print(f"{maior:.2f}")
    print(f"{menor:.2f}")
    print(f"{alturaf/mulheres:.2f}")
    print(f"{qtde_homens:.0f}")
        
    

if __name__ == '__main__':
    main()