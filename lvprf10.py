def main():
    #Declarar variaveis
    total_mulheres = float(0)
    total_homens = float(0)
    maior_altura = float(0)
    menor_altura = float(10)
    total_altura_mulheres = (0)

    #Entrada de dados
    for i in range(5):
        genero = input()
        altura = float(input())
        if genero == "f":
            total_mulheres += 1
            total_altura_mulheres += altura
        else:
            total_homens += 1

        if altura > maior_altura:
            maior_altura = altura
        elif altura < menor_altura:
            menor_altura = altura

        

    #Saida de dados
    print(maior_altura)
    print(menor_altura)
    print(total_altura_mulheres/total_mulheres)
    print(f"{total_homens:.0f}")

        
        
    
if __name__ == '__main__':
    main()