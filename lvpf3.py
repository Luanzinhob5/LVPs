def main():
    #Declarar variaveis
    valor = float(0)
    final = float(0)
    
    #Entrada de dados
    valor = float(input())

    
    #Processos
    if valor < 100:
        final = (valor*0.95)
        print(f"Valor final com desconto: R$ {final:.2f}")
    elif valor <= 500:
        final = (valor*0.90)
        print(f"Valor final com desconto: R$ {final:.2f}")
    elif valor > 500:
        final = (valor*0.85)
        print(f"Valor final com desconto: R$ {final:.2f}")

if __name__ == '__main__':
    main()