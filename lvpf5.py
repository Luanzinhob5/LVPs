def main():
    #Declarar variaveis
    idade = int(0)
    
    #Entrada de dados
    idade = int(input())

    #Processos
    if idade <= 10:
        print("Categoria: Infantil")
    elif idade <= 15:
        print("Categoria: Juvenil")
    elif idade <= 20:
        print("Categoria: Júnior")
    elif idade <= 30:
        print("Categoria: Profissional")
    else:
        print("Categoria: Sênior")
if __name__ == '__main__':
    main()