import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_sistema():
    
    print("-" * 60)
    print("CINEMAX".center(60))
    print("-" * 60)

while True: # loop principal
    menu_escolha = ["[1] Filmes em cartaz", "[2] Entrar/Cadastrar", "[3] Sair"]
    menu_sistema()
    
    for i in menu_escolha:
        print(i)
        
    resposta = input("Digite sua escolha: ")
    
    limpar_console()
    
    while True: # loop escolha
        
        if resposta == "1": # primeira escolha
            menu_sistema()
            
            # Inicio do modulo
            
            print("[1] Sair")
            
            if input("Digite sua escolha: ") == "1":
                limpar_console()
                break
            else:
                limpar_console()
                print(" ")
                print("****Digite um número válido!****".center(60))
                print(" ")
                
        elif resposta == "2": # segunda escolha
            menu_sistema()
            
            # Inicio do modulo
            
            print("[1] Entrar")
            print("[2] Cadastrar-se")
            print("[3] Sair")
            
            if input("Digite sua escolha: ") == "3":
                limpar_console()
                break
            else:
               limpar_console()
               print(" ")
               print("****Digite um número válido!****".center(60))
               print(" ")
            
        elif resposta == "3": # terceira escolha
            menu_sistema()
            print("Obrigado pela preferência, volte sempre!".center(60))
            print("-" * 60)
            exit()
        else:
            print(" ")
            print("****Digite um número válido!****".center(60))
            print(" ")
            break