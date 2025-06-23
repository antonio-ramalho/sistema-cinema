
import filmes
import utils_armazenamento as u_a
import modulo_salas as m_s

while True: # loop principal
    u_a.cabecalho_cinemax()
    resposta = u_a.menu_sistema()
    u_a.limpar_console()
          
    while True: # loop escolha
        
        if resposta == "1": # primeira escolha do loop
            
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
                
        elif resposta == "2": # segunda escolha do loop
                
            # Inicio do modulo salas e sessoes
            if m_s.modulo_filmes_salas() == True:
                break
            # Fim do modulo 
        elif resposta == "3": # terceira escolha do loop
            u_a.cabecalho_cinemax()
            print("Obrigado pela preferência, volte sempre!".center(60))
            print("-" * 60)
            exit()
        else: # Tudo aqui que não aparece na tela
            u_a.msg_numero_valido()
            break
        