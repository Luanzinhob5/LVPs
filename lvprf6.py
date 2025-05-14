def main():
    #Declarar variaveis
    numero = int(0)
    total_p = int(0)
    total_n = int(0)
    x = int(0)
    #Entrada de dados

    #Processos
    for n in range(5):
        numero = int(input())
        if numero > 0:
            total_p += numero
        else:
            total_n += numero
            x += 1
    print(f"{total_p:.0f}")
    print(f"{total_n/x:.1f}")
if __name__ == '__main__':
    main()