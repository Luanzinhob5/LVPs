def main():
    #Declarar variaveis
    velocidade = int(0)
    
    #Entrada de dados
    velocidade = int(input())

    #Processos
    if velocidade < 40:
        print("Muito Lento")
    elif velocidade <= 60:
        print("Lento")
    elif velocidade <= 80:
        print("Velocidade Permitida")
    elif velocidade <= 100:
        print("Acima do Limite")
    else:
        print("Multa Grave")
if __name__ == '__main__':
    main()