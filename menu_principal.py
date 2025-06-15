
import filmes
import utils_armazenamento as u_a

while True: # loop principal
    u_a.cabecalho_cinemax()
    resposta = u_a.menu_sistema()
    u_a.limpar_console()
          
    while True: # loop escolha
        if resposta == "1": # primeira escolha
            
            u_a.cabecalho_cinemax()
            filmes.mostrar_filmes(filmes.catalogo)
                
            print("[1] Sair")
            print(" ")
            
            if int(input("Digite sua escolha: ")) == 1:
                u_a.limpar_console()
                break
            else:
                u_a.limpar_console()
                u_a.msg_numero_valido()
        elif resposta == "2": # segunda escolha
            u_a.cabecalho_cinemax()
                
            # Inicio do modulo 
                
            print("[1] Entrar")
            print("[2] Cadastrar-se")
            print("[3] Sair")
                
            if int(input("Digite sua escolha: ")) == 3:
                u_a.limpar_console()
                break
            else:
                u_a.limpar_console()
                u_a.msg_numero_valido()  
        elif resposta == "3": # terceira escolha
            u_a.cabecalho_cinemax()
            print("Obrigado pela preferência, volte sempre!".center(60))
            print("-" * 60)
            exit()
        else:
            u_a.msg_numero_valido()
            break