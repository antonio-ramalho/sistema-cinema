import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_sistema():
    print("-" * 60)
    print("CINEMAX".center(60))
    print("-" * 60)

while True:
    menu_sistema()
    
    print("[1] Filmes em cartaz")
    print("[2] Entrar/Cadastrar")
    print("[3] Sair")
    
    resposta = input("Digite sua escolha: ")
    
    while True:
        if resposta == "1":
            limpar_console()
            menu_sistema()
            
            # Inicio do modulo
        elif resposta == "2":
            limpar_console()
            menu_sistema()
            
            # Inicio do modulo
        elif resposta == "3":
            print("-" * 60)
            print("Obrigado pela preferência, volte sempre!".center(60))
            exit()
        else:
            print("Digite um número válido!")
        