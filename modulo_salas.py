
import os
import json
import utils_armazenamento as u_a

# Funções graficas de armazenamento e lista de salas

def carregar_salas(nome_arquivo='salas.json'):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []

def salvar_salas(salas, nome_arquivo='salas.json'):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(salas, arquivo, ensure_ascii=False, indent=4)

salas = carregar_salas()

# Funções dos menus
   
def menu_sistema():
    menu_opcoes = ["[1] Salas de cinema", "[2] Sair"] 

    for i in menu_opcoes:
        print(i)
        
    resposta = input("Digite a opção que você escolheu: ")
    
    return resposta

def menu_filmes():
    menu_filmes_opcoes = ["[1] Ver sala específica", "[2] Cadastrar sala", "[3] Sair"] 

    for i in menu_filmes_opcoes:
        print(i)
        
    menu_filmes_resposta = input("Digite a opção que você escolheu: ")
    
    return menu_filmes_resposta

def menu_cadastra_sessao():
    menu_cadastra_sessao_opcoes = ["[1] Cadastrar sessão", "[2] Sair"] 

    for i in menu_cadastra_sessao_opcoes:
        print(i)
        
    menu_cadastra_sessao_resposta = input("Digite a opção que você escolheu: ")
    
    return menu_cadastra_sessao_resposta

# Funções da sala

def pegar_proximo_id_sala(salas_list):
    
    if not salas_list: 
        return 1 
    else:
        max_id = max(sala['sala_id'] for sala in salas_list)
        return max_id + 1

def cadastra_sala(salas_existentes): 
    
    nome_sala = ""
    
    while not nome_sala.strip():
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        print("CADASTRO DE NOVA SALA".center(60))
        
        sala_id_gerado = pegar_proximo_id_sala(salas_existentes)
        print(f"ID da nova sala: {sala_id_gerado}")
        nome_sala = input("Digite o nome da sala: ").strip()
        
        if not nome_sala:
            u_a.msg_numero_valido()
            input("Pressione Enter para tentar novamente...")

    numero_assentos_int = None
    while numero_assentos_int is None:
        
        try:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print(f"Cadastrando sala: {nome_sala} (ID: {sala_id_gerado})")
            assentos_input = input("Digite o número de assentos: ")
            numero_assentos_int = int(assentos_input)
            
            if numero_assentos_int <= 0: 
                raise ValueError 
        
        except ValueError:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print(f"***********************".center(60))
            print("Por favor, digite um número inteiro positivo para os assentos.".center(60))
            print(f"***********************".center(60))
            input("Pressione Enter para tentar novamente...")
            numero_assentos_int = None 

    quantidade_sessoes_inicial = 0

    return nome_sala, sala_id_gerado, numero_assentos_int, quantidade_sessoes_inicial
    
def armazena_sala(nome_sala, sala_id, numero_assentos, salas, quantidade_sessoes):
    
    sala = {
        'nome_sala': nome_sala,
        'sala_id': sala_id,
        'numero_assentos': numero_assentos,
        'quantidade_sessoes': quantidade_sessoes,
    }
    
    salas.append(sala)
    salvar_salas(salas)
    
    return salas

def mostra_salas(salas):
    
    for sala in salas:
        print(" ")
        print(f"Sala {sala['nome_sala']}".center(60))
        print(f"Nome da sala: {sala['nome_sala']}")
        print(f"Número de matrícula da sala: {sala['sala_id']}")
        print(f"Número de assentos nessa sala: {sala['numero_assentos']}")
        print(f"Número de sessões nessa sala: {sala['quantidade_sessoes']}")
        print("-" * 60)
        
    if salas == []:
        print("Ainda não existe uma sala cadastrada!".center(60))
    
# funções da sessão

def cadastra_sessao(sala_sessao, numero_assentos_sala, sala_id):
    
    tempo_sessao = None 
    sala_sessao = sala_sessao
    id_sala = sala_id
    
    while tempo_sessao is None: 
        try:
            u_a.limpar_console() 
            u_a.cabecalho_cinemax()
            print(f"Cadastrando sessão para a Sala: {sala_sessao} (ID: {sala_id})")
            tempo_sessao = int(input("Digite o tempo [em minutos] total da sessão: "))
        except ValueError:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            u_a.msg_numero_valido()
            input("Pressione Enter para tentar novamente...") 

    horario_inicio = input("Digite o horário de início da sessão (Ex: 09:00): ")
    horario_termino = input("Digite o horário de término da sessão (Ex: 11:00): ")
    
    numero_assentos_sessao = numero_assentos_sala
    
    return sala_sessao, tempo_sessao, horario_inicio, horario_termino, numero_assentos_sessao, id_sala 

def mostra_sessao(sala):
     
    if 'sessoes_associadas' in sala:
        print(f"Sala {sala['nome_sala']}".center(60).upper())
        for sessao in sala['sessoes_associadas']:
            print(" ")
            print(f"  ID da Sessão: {sessao['id_sessao']}")
            print(f"  Sala da Sessão: {sessao['sala_sessao']}")
            print(f"  ID da sala: {sessao['id_sala']}")
            print(f"  Horário de Início: {sessao['horario_inicio']}")
            print(f"  Horário de Término: {sessao['horario_termino']}")
            print(f"  Tempo da Sessão: {sessao['tempo_sessao']} minutos")
            print(f"  Número de assentos: {sessao['numero_assentos']}")
            print("-" * 60)
    else: 
        print("Ainda não existem sessões cadastradas nessa sala.".center(60))
   
def pegar_proximo_id_sessao(sessoes_associadas_da_sala):

    if not sessoes_associadas_da_sala:
        return 1 
    else:
        max_id = max(sessao['id_sessao'] for sessao in sessoes_associadas_da_sala)
        return max_id + 1
        
# Terminal de gerenciamento

def gerenciar_sala_selecionada(sala_selecionada_id, salas_data):

    sala_encontrada = None
    
    # Busca por sala sala selecionada
    for sala in salas_data:
        if sala_selecionada_id == sala['sala_id']:
            sala_encontrada = sala
            break 

    if sala_encontrada:
        u_a.cabecalho_cinemax()
        mostra_sessao(sala_encontrada)

        while True: # Loop para o menu de opções da sala (cadastrar sessão, sair)
            menu_cadastra_sessao_resposta = menu_cadastra_sessao()
            u_a.limpar_console() 

            if menu_cadastra_sessao_resposta == "1": # Cadastrar sessão
                u_a.cabecalho_cinemax()

                if 'sessoes_associadas' not in sala_encontrada:
                    sala_encontrada['sessoes_associadas'] = []
                    
                proximo_id_sessao = pegar_proximo_id_sessao(sala_encontrada['sessoes_associadas'])

                sala_sessao, tempo_sessao, horario_inicio, horario_termino, \
                numero_assentos_sessao, id_sala_sessao = cadastra_sessao(
                    sala_encontrada['nome_sala'], sala_encontrada['numero_assentos'], sala_encontrada['sala_id']
                )

                # Cria o dicionário da nova sessão
                nova_sessao = {
                    'sala_sessao': sala_sessao,
                    'id_sessao': proximo_id_sessao,
                    'id_sala': id_sala_sessao,
                    'horario_inicio': horario_inicio,
                    'horario_termino': horario_termino,
                    'tempo_sessao': tempo_sessao,
                    'numero_assentos': numero_assentos_sessao,
                }
                
                sala_encontrada['sessoes_associadas'].append(nova_sessao)
                sala_encontrada['quantidade_sessoes'] = len(sala_encontrada['sessoes_associadas'])
               
                salvar_salas(salas_data) 
                u_a.limpar_console()
                u_a.cabecalho_cinemax()
                print("Sessão cadastrada com sucesso!".center(60))
                mostra_sessao(sala_encontrada) 

            elif menu_cadastra_sessao_resposta == "2": # Sair do menu de cadastro de sessão
                u_a.limpar_console()
                break 
            else:
                u_a.limpar_console()
                u_a.msg_numero_valido()
                u_a.cabecalho_cinemax() 
                mostra_sessao(sala_encontrada) 

    else: # Esta sala não foi encontrada no loop
        print("Essa sala ainda não existe.".center(60))
    
    return

def modulo_filmes_salas():
    while True: #loop principal
        u_a.cabecalho_cinemax()
        resposta = menu_sistema()
        u_a.limpar_console()
                
        while True: #loop principal
                    
            if resposta == "1": # Ver salas 
                u_a.cabecalho_cinemax()
                mostra_salas(salas)
                menu_filmes_resposta = menu_filmes()
                            
                if menu_filmes_resposta == "1": # sala especifica
                            
                    try:
                        sala_selecionada_id = int(input("Digite o número de matrícula da sala que você selecionou: "))
                        u_a.limpar_console()
                        gerenciar_sala_selecionada(sala_selecionada_id, salas)              
                    except ValueError:
                        u_a.limpar_console()
                        u_a.msg_numero_valido()
                                                
                elif menu_filmes_resposta == "2": # cadastrar sala
                    try:
                        u_a.limpar_console()
                        u_a.cabecalho_cinemax()
                        nome_sala, sala_id, numero_assentos, quantidade_sessoes = cadastra_sala(salas)
                        armazena_sala(nome_sala, sala_id, numero_assentos, salas, quantidade_sessoes)
                        u_a.limpar_console()
                        print("Sala cadastrada com sucesso!".center(60))
                    except ValueError:
                        u_a.limpar_console()
                        u_a.msg_numero_valido()
                elif menu_filmes_resposta == "3": # sair
                    u_a.limpar_console()
                    break
                else: #quaquer outra opção
                    u_a.limpar_console()
                    u_a.msg_numero_valido()
            elif resposta == "2": # Sair
                u_a.limpar_console()
                return True
            else: # qualquer outra opção
                u_a.msg_numero_valido()
                break