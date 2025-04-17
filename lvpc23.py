def main():
    #Declarar variaveis
    idadeh1 = int(0)
    idadeh2 = int(0)
    idadem1 = int(0)
    idadem2 = int(0)

    #Entrada de dados
    idadeh1 = int(input())
    idadeh2 = int(input())
    idadem1 = int(input())
    idadem2 = int(input())
    
    #Processos e Saida de dados
    if idadeh1 > idadeh2 and idadem1 > idadem2:
        print(f'{idadeh1 + idadem2} {idadeh2*idadem1}')
    elif idadeh2 > idadeh1 and idadem1 > idadem2:
        print(f'{idadeh2 + idadem2} {idadeh1*idadem1}')
    elif idadeh2 > idadeh1 and idadem2 > idadem1:
        print(f'{idadeh2 + idadem1} {idadeh1*idadem2}')
    else:
        print(f'{idadeh1 + idadem1} {idadeh2*idadem2}')


if __name__ == '__main__':
    main()