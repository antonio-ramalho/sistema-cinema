# funções gráficas e de armazenamento usadas em todo o sistema

import os

def menu_sistema(): 
    menu_escolha = ["[1] Filmes em cartaz", "[2] Entrar/Cadastrar", "[3] Sair"]
    
    for i in menu_escolha:
        print(i)
    
    resposta = input("Digite sua escolha: ")
    
    return resposta

def escolha_admin():
    menu_escolha_admin = ["[1] Cadastrar filmes", "[2] Excluir filme","[3] Listar Usuários","[4] Excluir Usuário", \
    "[5] Cadastrar salas e sessões", "[0] Sair"]
    for i in menu_escolha_admin:
        print(i)
    
    resposta_admin = input("Digite sua escolha: ")
    
    return resposta_admin

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho_cinemax():
    print("-" * 60)
    print("CINEMAX".center(60))
    print("-" * 60)

def msg_numero_valido():
    print(" ")
    print("****Digite um número válido!****".center(60))
    print(" ")