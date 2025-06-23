
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
            
            if input("Digite sua escolha: ") == "1":
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
                
            if input("Digite sua escolha: ") == "3":
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


    dados_usuario = login()
    if dados_usuario:
        while True:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print(f"Bem-vindo(a), {dados_usuario['nome']}!")
            print("\n--- MENU DE USUÁRIO ---")

            # Menu completo com todas as opções planejadas:
            print("[1] Comprar Ingresso")
            print("[2] Ver Meu Histórico de Compras")
            print("[3] Avaliar um Filme")
            print("[4] Modificar Meus Dados")
            print("[5] Logout")
            
            resposta_menu = input("\nDigite sua escolha: ")

            if resposta_menu == "1":
                print("\nFunção de Comprar Ingresso (a ser implementada).")
                print("Guiará o usuário para: Escolher Filme > Horário > Sala > Pagamento.")
                u_a.input_continuar()
            
            elif resposta_menu == "2":
                print("\nFunção de Ver Histórico (a ser implementada).")
                u_a.input_continuar()

            elif resposta_menu == "3":
                print("\nFunção de Avaliar Filme (a ser implementada).")
                u_a.input_continuar()

            elif resposta_menu == "4":
                # Esta função já existe e está funcionando
                Modifica_propria_conta(dados_usuario)
            
            elif resposta_menu == "5":
                print("\nLogout realizado com sucesso!")
                u_a.input_continuar()
                break # Encerra o loop e a sessão do usuário
    else:
        print("\nFalha no login.")
        u_a.input_continuar()