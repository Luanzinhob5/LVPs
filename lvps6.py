def main():
    #Declarar variaveis
    entrada = str()

    entrada = input()


    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
    print(f"{entrada[:2]} de {meses[int(entrada[3:5])]} de {entrada[6:10]}")
                
if __name__ == '__main__':
    main()