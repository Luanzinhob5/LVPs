def main():
    #Declarar variaveis
    nota = float(0)
    dias = float(0)
    
    #Entrada de dados
    nota = float(input())
    dias = float(input())
    
    #Processos
    nota_final = nota - ((dias * 0.1) * nota)
    if nota_final < 0:
        print(f"Nota final: 0.00")
    else:
        print(f"Nota final: {nota_final:.2f}")

if __name__ == '__main__':
    main()