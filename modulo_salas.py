
import os
import json
import utils_armazenamento as u_a
import filmes

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

catalogo_filmes = filmes.catalogo

todos_os_horarios_possiveis = [
    "10:00-12:00", "12:30-14:30", "15:00-17:00", "17:30-19:30", "20:00-22:00", "22:30-00:30"
]

# Funções dos menus

def menu_filmes():
    menu_filmes_opcoes = ["[1] Ver sala específica", "[2] Cadastrar sala", "[3] Excluir sala", "[4] Sair"] 

    for i in menu_filmes_opcoes:
        print(i)
        
    menu_filmes_resposta = input("Digite a opção que você escolheu: ")
    
    return menu_filmes_resposta

def menu_cadastra_sessao():
    menu_cadastra_sessao_opcoes = ["[1] Cadastrar sessão", "[2] Excluir sessão", "[3] Colocar filme em sessão", "[4] Sair"] 

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

def gercao_Id_e_nome_sala(salas_existentes):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("CADASTRO DE NOVA SALA".center(60))
        
    sala_id_gerado = pegar_proximo_id_sala(salas_existentes)
    print(f"ID da nova sala: {sala_id_gerado}")
    nome_sala = input("Digite o nome da sala: ").strip()
        
    if not nome_sala:
        u_a.msg_numero_valido()
        input("Pressione Enter para tentar novamente...")
    
    return sala_id_gerado, nome_sala

def geracao_numero_assentos_sala(sala_id_gerado, nome_sala):
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
        
    return numero_assentos_int

def cadastra_sala(salas_existentes):
    
    nome_sala = ""
    
    while not nome_sala.strip():
        sala_id_gerado, nome_sala = gercao_Id_e_nome_sala(salas_existentes)

        numero_assentos_int = None
        
        while numero_assentos_int is None:
            numero_assentos_int = geracao_numero_assentos_sala(sala_id_gerado, nome_sala)

        quantidade_sessoes_inicial = 0

    return {
            'nome_sala': nome_sala, 
            'sala_id': sala_id_gerado,
            'numero_assentos': numero_assentos_int,
            'quantidade_sessoes': quantidade_sessoes_inicial
    }
    
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
        
def buscar_sala(sala_selecionada_id, salas):

    sala_encontrada = None
    for sala in salas:
        if sala_selecionada_id == sala['sala_id']:
            sala_encontrada = sala
            break 
        
    return sala_encontrada
    
def buscar_sala_excluir():
    sala_encontrada = None
    
    while sala_encontrada is None:
        try:
            sala_selecionada_exclusao_id = int(input("Digite o número de matrícula da sala que você selecionou: "))
            sala_encontrada = buscar_sala(sala_selecionada_exclusao_id, salas)
            return sala_encontrada
        except ValueError:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print("Digite um número valido.")
            input("Pressione Enter para tentar novamente...")
            u_a.limpar_console()
            u_a.cabecalho_cinemax()

def excluir_sala():
    
    sala_encontrada = buscar_sala_excluir()
        
    if sala_encontrada: 
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        mostra_sessao(sala_encontrada)
         
        try:       
            if input("Você deseja excluir essa sala e todas as suas sessões [S/N]: ").upper() == "S":
                salas.remove(sala_encontrada)
                u_a.limpar_console()
                print(f"Sala excluida com sucesso!".center(60))      
            else:
                u_a.limpar_console()  
                print(f"Sala não excluida com sucesso!".center(60))            
        except ValueError:
            u_a.cabecalho_cinemax()
            u_a.limpar_console()
            u_a.msg_numero_valido()
            input("Pressione Enter para tentar novamente...")
    else:
        u_a.limpar_console()
        print("Essa sala ainda não existe.".center(60))
        
# funções da sessão

def calcula_horarios_disponiveis(sala_encontrada):

    horarios_ocupados_sala = sala_encontrada.get('horarios_ocupados', [])
    
    horarios_disponiveis = [
        h for h in todos_os_horarios_possiveis if h not in horarios_ocupados_sala
    ]
    return horarios_disponiveis

def valida_horarios_disponiveis(sala_encontrada, horarios_disponiveis):

    if not horarios_disponiveis:
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        print(f"Não há horários disponíveis para a Sala '{sala_encontrada['nome_sala']}'.")
        input("Pressione Enter para voltar ao menu...")
        return False 
    
    return True 

def apresentar_horarios(sala_encontrada, horarios_disponiveis):
    
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print(f"CADASTRO DE SESSÃO PARA A SALA: {sala_encontrada['nome_sala'].upper()}")
    print("-" * 60)
    print("Horários disponíveis:".center(60))
        
    for i, horario_bloco in enumerate(horarios_disponiveis):
        print(f"[{i+1}] {horario_bloco}")
    print("-" * 60)
    
def coletar_escolha_horario(sala_encontrada, horarios_disponiveis):

    horario_selecionado = None
    
    while horario_selecionado is None: 
        apresentar_horarios(sala_encontrada, horarios_disponiveis) 
        try:
            opcao_horario = int(input("Escolha o número do horário desejado: "))
            if 1 <= opcao_horario <= len(horarios_disponiveis):
                horario_selecionado = horarios_disponiveis[opcao_horario-1]
                return horario_selecionado
            else:
                raise ValueError 
        except ValueError:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            u_a.msg_numero_valido()
            input("Pressione Enter para tentar novamente...")

def cadastra_horario_sessao(sala_encontrada):

    horarios_disponiveis = calcula_horarios_disponiveis(sala_encontrada)
    
    if not valida_horarios_disponiveis(sala_encontrada, horarios_disponiveis):
        return None, None, None 

    horario_selecionado = coletar_escolha_horario(sala_encontrada, horarios_disponiveis)
    
    if horario_selecionado is None:
        return None, None, None
    
    horario_inicio = horario_selecionado.split('-')[0].strip()
    horario_termino = horario_selecionado.split('-')[1].strip()
    
    return horario_inicio, horario_termino, horario_selecionado

def cadastra_tempo_sessao(sala_encontrada, horario_selecionado_bloco): 
    tempo_sessao = None
    
    while tempo_sessao is None:
        try:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print(f"Cadastrando sessão para a Sala: {sala_encontrada['nome_sala']} - Horário: {horario_selecionado_bloco}")
            tempo_input = input("Digite o tempo [em minutos] total da sessão: ")
            tempo_sessao = int(tempo_input)
            if tempo_sessao <= 0:
                raise ValueError("O tempo da sessão deve ser um número inteiro positivo.")
        except ValueError as e:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            u_a.msg_numero_valido()
            print(f"***********************".center(60))
            print(f"Erro: {e}".center(60)) 
            print(f"***********************".center(60))
            input("Pressione Enter para tentar novamente...")
            tempo_sessao = None
             
    return tempo_sessao

def cadastra_sessao(sala_encontrada): 
    
    horario_inicio, horario_termino, horario_selecionado_bloco = cadastra_horario_sessao(sala_encontrada)
    
    if horario_selecionado_bloco is None: 
        return None

    tempo_sessao = cadastra_tempo_sessao(sala_encontrada, horario_selecionado_bloco)
    
    if tempo_sessao is None:
        return None

    return {
        'sala_sessao': sala_encontrada['nome_sala'],
        'horario_bloco': horario_selecionado_bloco, 
        'horario_inicio': horario_inicio,
        'horario_termino': horario_termino,
        'tempo_sessao': tempo_sessao,
        'numero_assentos': sala_encontrada['numero_assentos'], 
        'id_sala': sala_encontrada['sala_id']
    }

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
       
def buscar_sessao(sessao_selecionada_exclusao_id, sala_encontrada):
    sessao_encontrada = None
    
    for sessao in sala_encontrada['sessoes_associadas']:
        if sessao_selecionada_exclusao_id == sessao['id_sessao']:
            sessao_encontrada = sessao
            break
    
    return sessao_encontrada
             
def buscar_sessao_excluir(sala_encontrada):
    sessao_encontrada = None
    
    while sessao_encontrada is None:
        try:
            sessao_selecionada_exclusao_id = int(input("Digite o número de matrícula da sessão que você selecionou: "))
            sessao_encontrada = buscar_sessao(sessao_selecionada_exclusao_id, sala_encontrada)
            return sessao_encontrada
        except ValueError:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print("Digite um número valido.")
            input("Pressione Enter para tentar novamente...")
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            
def checagem_se_sessao_existe(sala_encontrada):
    
    if not sala_encontrada.get('sessoes_associadas'): 
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        print(f"Não há sessões cadastradas para a Sala '{sala_encontrada['nome_sala']}'.")
        input("Pressione Enter para voltar ao menu...")
        return True
    
def excluir_sessao(sala_encontrada, salas_data):
    
    if checagem_se_sessao_existe(sala_encontrada):
        return
    
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    mostra_sessao(sala_encontrada)
        
    sessao_encontrada_para_exluir = buscar_sessao_excluir(sala_encontrada)
    
    if sessao_encontrada_para_exluir: 
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        print(f"Sessão selecionada para exclusão:")
        print(f"  ID: {sessao_encontrada_para_exluir['id_sessao']} | Horário: {sessao_encontrada_para_exluir.get('horario_bloco', 'N/A')}")
        print("-" * 60)
        confirmacao = input("Você deseja REALMENTE excluir essa sessão? [S/N]").upper()
        
        if confirmacao == "S":
            sala_encontrada['sessoes_associadas'].remove(sessao_encontrada_para_exluir)
            
            if 'horarios_ocupados' in sala_encontrada and \
               sessao_encontrada_para_exluir.get('horario_bloco') in sala_encontrada['horarios_ocupados']:
                sala_encontrada['horarios_ocupados'].remove(sessao_encontrada_para_exluir['horario_bloco'])
            
            sala_encontrada['quantidade_sessoes'] = len(sala_encontrada['sessoes_associadas'])
            salvar_salas(salas_data)
            
            u_a.limpar_console()
            print(f"Sessão excluida com sucesso!".center(60))      
        else:
            u_a.limpar_console()  
            print(f"Sessão não excluida com sucesso!".center(60))            
    else:
        u_a.limpar_console()
        print("Essa sessão ainda não existe.".center(60))

def escolher_filme_para_sessao(filmes):
    
    escolha = input("Digite o nome do filme que você escolheu: ")
    
    filme_escolhido_nome = None
    
    for filme in filmes:
        if escolha == filme['nome']:
            filme_escolhido_nome = filme['nome']
            break
    
    return {
        'nome_filme': filme_escolhido_nome,
    }
    
def colocar_filme_em_sessao(filme_escolhido):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    for sala in salas:
        
        print(" ")
        print(f"Sala {sala['nome_sala']}".center(60))
        print(f"Nome da sala: {sala['nome_sala']}")
        print(f"Número de matrícula da sala: {sala['sala_id']}")
        print(f"Número de assentos nessa sala: {sala['numero_assentos']}")
        print(f"Número de sessões nessa sala: {sala['quantidade_sessoes']}")
        print("-" * 60)
        
        mostra_sessao(sala)
    
    while True:   
        resposta = int(input("Digite o Id da sala que você pretende colocar o filme: "))
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        
        sala_encontrada = buscar_sala(resposta, salas)
        
        print(f"sala {sala_encontrada['nome_sala']}: ".upper())
        mostra_sessao(sala_encontrada)
        
        resposta_sessao = int(input("Digite o ID da sessão que você deseja colocar o filme: "))
        
        sessao_encontrada = buscar_sessao(resposta_sessao, sala_encontrada)
        
        sessao_encontrada['filme_escolhido'] = filme_escolhido
        salvar_salas(salas)
        
        if input("Deseja colocar mais algum filme em alguma sessão? [S/N]").upper() == "S":
            pass
        else:
            break
    
# Funções do terminal de gerenciamento de sala selecionada

def gerenciar_sala_selecionada(sala_selecionada_id, salas_data):
    
    # Busca por sala sala selecionada
    sala_encontrada = buscar_sala(sala_selecionada_id, salas_data)

    # Se essa sala exister
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
                
                nova_sessao_dados = cadastra_sessao(sala_encontrada) 

                if nova_sessao_dados: # Se a sessão foi criada com sucesso 
                    
                    proximo_id_sessao = pegar_proximo_id_sessao(sala_encontrada.get('sessoes_associadas', []))
                    nova_sessao_dados['id_sessao'] = proximo_id_sessao 

                    if 'sessoes_associadas' not in sala_encontrada:
                        sala_encontrada['sessoes_associadas'] = []
                        
                    sala_encontrada['sessoes_associadas'].append(nova_sessao_dados)
                    
                    if 'horarios_ocupados' not in sala_encontrada:
                        sala_encontrada['horarios_ocupados'] = []
                        
                    sala_encontrada['horarios_ocupados'].append(nova_sessao_dados['horario_bloco'])
                    sala_encontrada['quantidade_sessoes'] = len(sala_encontrada['sessoes_associadas'])
                    salvar_salas(salas_data)
              
                    u_a.limpar_console()
                    u_a.cabecalho_cinemax()
                    print("Sessão cadastrada com sucesso!".center(60))
                    mostra_sessao(sala_encontrada)
                else:
                    u_a.cabecalho_cinemax()
                    mostra_sessao(sala_encontrada) 
            elif menu_cadastra_sessao_resposta == "2": # Excluir sessão
                u_a.limpar_console()
                u_a.cabecalho_cinemax()
                excluir_sessao(sala_encontrada, salas_data)
                salvar_salas(salas)
                u_a.cabecalho_cinemax()
                mostra_sessao(sala_encontrada)
            elif menu_cadastra_sessao_resposta == "3": # Sair do menu de cadastro de sessão 
                u_a.limpar_console()
                break
            else: # Caso o usuario escolha qualquer outra coisa
                u_a.limpar_console()
                u_a.msg_numero_valido()
                u_a.cabecalho_cinemax() 
                mostra_sessao(sala_encontrada) 
    else: # Esta sala não foi encontrada no loop
        print("Essa sala ainda não existe.".center(60))

# Função módulo, ela une todo o módulo para o código principal

def modulo_filmes_salas():
        u_a.limpar_console()
        while True: #loop principal
                
                u_a.cabecalho_cinemax()
                mostra_salas(salas)
                menu_filmes_resposta = menu_filmes()
                            
                if menu_filmes_resposta == "1": # Ver sala especifica      
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
                        nova_sala = cadastra_sala(salas)
                        salas.append(nova_sala)
                        salvar_salas(salas)
                        u_a.limpar_console()
                        print("Sala cadastrada com sucesso!".center(60))
                    except ValueError:
                        u_a.limpar_console()
                        u_a.msg_numero_valido()
                elif menu_filmes_resposta == "3": # Excluir sala
                    u_a.limpar_console()
                    u_a.cabecalho_cinemax()
                    excluir_sala()
                    salvar_salas(salas)
                elif menu_filmes_resposta == "4": # Sair
                    u_a.limpar_console()
                    break
                else: # Qualquer outra opção que o usuario escolher
                    u_a.limpar_console()
                    u_a.msg_numero_valido()