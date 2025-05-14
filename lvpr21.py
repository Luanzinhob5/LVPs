def main():
    #Declarar variaveis
    off = True
    sim = str()
    escolha = str()
    numero_1 = float(0)
    numero_2 = float(0)
    operacao = float(0)



    while off:
        #Entrada do sim
        sim = input()
        if sim == "s":
            #entrada da escolha
            operacao = 0
            escolha = input()
            if escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4" or escolha == "5" or escolha == "6":
                numero_1 = float(input())
                numero_2 = float(input())

                if escolha == "1":
                    operacao = numero_1 + numero_2
                
                elif escolha == "2":
                    operacao = numero_1 - numero_2
                
                elif escolha == "3":
                    operacao = numero_1 * numero_2

                elif escolha == "4":
                    operacao = numero_1 / numero_2

                elif escolha == "5":
                    operacao = numero_1 ** numero_2

                elif escolha == "6":
                    operacao = numero_1 ** ( 1/numero_2 )

                if operacao == 0:
                    operacao == 0
                else:
                    print(operacao)
                    
                #Saida de Erro
            else:
                print(f"OPERACAO INVALIDA")
            

                #Processo da operacao escolhida
                
                

        else:
            off = False


        
        
    
if __name__ == '__main__':
    main()