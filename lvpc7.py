def main():
    #Declarar variaveis
    ano = int(0)
   
    
    #Entrada de dados
    ano = int(input())
   
    
    #Processos
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{ano} É BISSEXTO')
    else:
        print(f'{ano} NÃO É BISSEXTO')

if __name__ == '__main__':
    main()