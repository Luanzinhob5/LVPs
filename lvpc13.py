def main():
    #Declarar variaveis
    a = float(0)
    b = float(0)
    c = float(0)

    #Entrada de dados
    a = float(input())
    b = float(input())
    c = float(input())
   
    #Processos
    
    primeiro = (-b+(b**2-4*a*c)**0.5)/(2*a)
    segundo = (-b-(b**2-4*a*c)**0.5)/(2*a)
    
    #Saida de dados
    if primeiro == segundo:
        print(primeiro)
        
    elif primeiro == complex(primeiro):
        print('Não há raízes reais')

    else:
        print(primeiro, segundo)
        
if __name__ == '__main__':
    main()