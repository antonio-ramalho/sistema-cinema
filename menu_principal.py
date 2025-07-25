import filmes
import utils as u_a
import admin
import modulo_salas as m_s
import usuario
import dados
import time

while True: # loop principal
    u_a.cabecalho_cinemax()
    resposta = u_a.menu_sistema()
    u_a.limpar_console()

    while True: # loop escolha
        if resposta == "1": # primeira escolha (Filmes em Cartaz)
            
            u_a.cabecalho_cinemax()
            filmes.mostrar_filmes(filmes.catalogo)
                
            print("[1] Sair")
            print(" ")
            
            if input("Digite sua escolha: ") == "1": #Sair
                u_a.limpar_console()
                break
            else:
                u_a.limpar_console()
                u_a.msg_numero_valido()
        elif resposta == "2": # segunda escolha (Entrar/Cadastrar)
            u_a.cabecalho_cinemax()
                
            # Inicio do modulo 
                
            print("[1] Entrar")
            print("[2] Cadastrar-se")
            print("[3] Sair")

            escolha = input("Digite sua escolha: ")
            if escolha == "1": #Entrar
                u_a.limpar_console()
                u_a.cabecalho_cinemax()
                usuario_logado = admin.login()
                if usuario_logado:
                    usuarios = dados.carregar_usuarios()
                    eh_admin = usuarios[usuario_logado]['admin']

                    while True:
                        if eh_admin == True:
                            dados_completos = usuarios[usuario_logado]
                            u_a.limpar_console()
                            u_a.cabecalho_cinemax()
                            print('O que deseja fazer?')
                            resposta_admin = u_a.escolha_admin(dados_completos)
                            if resposta_admin == '1': #Cadastrar Filme
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                filmes.cadastra_filme(filmes.catalogo)
                                time.sleep(1)
                            elif resposta_admin == '2': #Excluir Filme
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                filmes.excluir_filme(filmes.catalogo)
                            elif resposta_admin == '3':
                                while True:
                                    u_a.limpar_console()
                                    u_a.cabecalho_cinemax()
                                    admin.listar_usuarios()
                                    
                                    if input('Digite 0 para sair ') == '0':
                                        break
                            elif resposta_admin == '4':
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                admin.exclui_usuario()
                                time.sleep(1)
                            elif resposta_admin == '5':
                                m_s.modulo_filmes_salas()
                            elif resposta_admin == '6':
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                filme_escolhido = filmes.escolher_filme(filmes.catalogo)
                                if filme_escolhido == None:
                                    print("O catálogo está vazio.".center(60))
                                    print("-" * 60)
                                    input("Digite enter...")
                                    pass
                                else:
                                    m_s.colocar_filme_em_sessao(filme_escolhido)

                            elif resposta_admin == '7': 
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                admin.definir_preco_filme()
                            
                            elif resposta_admin == '8': 
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                admin.mostrar_relatorios()

                            elif resposta_admin == '0':
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                print("Obrigado pela preferência, volte sempre!".center(60))
                                print("-" * 60)
                                break
                            else:
                                u_a.msg_numero_valido()
                        else:
                            dados_completos = usuarios[usuario_logado]
                            dados_completos['cpf'] = usuario_logado
                            u_a.limpar_console()
                            u_a.cabecalho_cinemax()
                            resposta_usuario = u_a.escolha_usuario(dados_completos)
                            if resposta_usuario == '1':
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                usuario.comprar_ingresso(dados_completos)
                            elif resposta_usuario == '2':
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                usuario.ver_historico(dados_completos)
                            elif resposta_usuario == "3":
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                usuario.avaliar_filme(dados_completos)
                            elif resposta_usuario == "4":
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                usuario.modifica_propria_conta(dados_completos)
                            elif resposta_usuario == "5":
                                u_a.limpar_console()
                                u_a.cabecalho_cinemax()
                                print("\nSaindo da sua conta...")
                                u_a.input_continuar()
                                u_a.limpar_console()
                                break
                            else:
                                u_a.msg_numero_valido
            elif escolha == "2": #Cadastrar Usuário
                u_a.limpar_console
                u_a.cabecalho_cinemax
                admin.menu_cadastro()
                time.sleep(1)
            elif escolha == "3": #Sair
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