# funções gráficas e de armazenamento usadas em todo o sistema

import os

def menu_sistema(): 
    menu_escolha = ["[1] Filmes em cartaz", "[2] Entrar/Cadastrar", "[3] Sair"]
    
    for i in menu_escolha:
        print(i)
    
    resposta = input("Digite sua escolha: ")
    
    return resposta

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

def input_continuar():
    input("\nPressione Enter para continuar...")