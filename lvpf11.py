import random

def main():
    #Declarar variaveis
    
    def chars():
        jogadas = 0
        end = True
        string = ""

        while end:
            dado = input()
            if dado == " ":
                end = False
            else:
                string += dado
                contagem = 0 
                jogadas += 1
                if jogadas == 1:
                    primeiro_dado = dado

            if primeiro_dado == 7 or primeiro_dado == 11:
                print(f"VOCÊ GANHOU JOGADAS = {jogadas}")

            elif primeiro_dado == 3 or primeiro_dado == 2 or primeiro_dado == 12 :
                print(f"CRAPS! VOCÊ PERDEU JOGADAS = {jogadas}")

            elif "7" in string:
                print(f"VOCÊ PERDEU JOGADAS = {jogadas}")

            elif dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado == 10:
                for letra in string:
                    if letra == str(dado):
                        contagem += 1
                if contagem == 2:
                    print(f"VOCÊ GANHOU JOGADAS = {jogadas}")

    chars()


        



            
                
                

    
        
            
            

if __name__ == '__main__':
    main()