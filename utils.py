# funções gráficas usadas em todo o sistema ou no sistema principal

import os

def input_continuar():
    input("\nPressione Enter para continuar...")

def menu_sistema(): 
    menu_escolha = ["[1] Filmes em cartaz", "[2] Entrar/Cadastrar", "[3] Sair"]
    
    for i in menu_escolha:
        print(i)
    
    resposta = input("Digite sua escolha: ")
    
    return resposta

def escolha_admin(dados_usuario):
    print(f"Bem-vindo(a), {dados_usuario['nome']}!")
    menu_escolha_admin = ["[1] Cadastrar filmes", "[2] Excluir filme","[3] Listar Usuários","[4] Excluir Usuário","[5] Salas e sessões", "[6] Cadastar filme na sessão","[0] Sair"]
    for i in menu_escolha_admin:
        print(i)
    
    resposta_admin = input("Digite sua escolha: ")
    
    return resposta_admin

def escolha_usuario(dados_usuario):
    print(f"Bem-vindo(a), {dados_usuario['nome']}!")
    menu_escolha_usuario = ["[1] Comprar Ingresso", "[2] Ver Meu Histórico de Compras", "[3] Avaliar um Filme", "[4] Modificar Meus Dados", "[5] Sair"]

    for i in menu_escolha_usuario:
        print(i)
    
    resposta_usuario = input("Digite sua escolha: ")
    
    return resposta_usuario

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