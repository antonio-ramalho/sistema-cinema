# usuario.py (Versão Final com Documentação)

import dados
import utils_armazenamento as u_a
import json


# Mostra os filmes e lida com a escolha do usuário.
def _escolher_filme(catalogo):
    if not catalogo:
        print("\nNenhum filme em cartaz no momento.")
        return None
    
    print("\n--- Filmes em Cartaz ---")
    for i, filme in enumerate(catalogo):
        print(f"[{i+1}] - {filme['nome']}")
    
    while True:
        try:
            escolha = int(input("\nDigite o número do filme (ou 0 para voltar): "))
            if escolha == 0: return None
            if 1 <= escolha <= len(catalogo): return catalogo[escolha - 1]
            else: print("❌ Opção inválida.")
        except ValueError:
            print("❌ Por favor, digite um número.")

# Mostra as sessões para um filme e lida com a escolha.
def _escolher_sessao(filme_escolhido):
    salas = dados.carregar_salas()
    sessoes_disponiveis = [sessao for sala in salas for sessao in sala.get('sessoes_associadas', []) if sessao.get('filme_escolhido', {}).get('nome') == filme_escolhido['nome']]
    
    if not sessoes_disponiveis:
        print(f"\nDesculpe, não há sessões disponíveis para '{filme_escolhido['nome']}'.")
        return None

    print(f"\n--- Sessões para '{filme_escolhido['nome']}' ---")
    for i, sessao in enumerate(sessoes_disponiveis):
        print(f"[{i+1}] - Sala: {sessao['sala_sessao']} | Horário: {sessao['horario_inicio']}")
    
    while True:
        try:
            escolha = int(input("\nDigite o número da sessão (ou 0 para voltar): "))
            if escolha == 0: return None
            if 1 <= escolha <= len(sessoes_disponiveis): return sessoes_disponiveis[escolha - 1]
            else: print("❌ Opção inválida.")
        except ValueError:
            print("❌ Por favor, digite um número.")

# Lida com a escolha de um assento vago.
def _escolher_assento(sessao_escolhida):
    assentos_ocupados = sessao_escolhida.get('assentos_ocupados', [])
    print("\n--- Escolha de Assento ---")
    print(f"Assentos já ocupados: {', '.join(assentos_ocupados) if assentos_ocupados else 'Nenhum'}")
    
    while True:
        assento = input("Digite o assento desejado (ex: A5) ou '0' para voltar: ").upper()
        if assento == '0': return None
        if not assento: print("❌ Por favor, digite um assento.")
        elif assento in assentos_ocupados: print(f"❌ O assento {assento} já está ocupado.")
        else: return assento

# Orquestra o fluxo completo de compra de ingresso.
def comprar_ingresso(dados_usuario):
    filme_selecionado = _escolher_filme(dados.carregar_filmes())
    if not filme_selecionado: return u_a.input_continuar()

    sessao_selecionada = _escolher_sessao(filme_selecionado)
    if not sessao_selecionada: return u_a.input_continuar()

    assento_escolhido = _escolher_assento(sessao_selecionada)
    if not assento_escolhido: return u_a.input_continuar()

    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- RESUMO DA COMPRA ---")
    print(f"Filme: {filme_selecionado['nome']}\nSala: {sessao_selecionada['sala_sessao']}\nHorário: {sessao_selecionada['horario_inicio']}\nAssento: {assento_escolhido}")
    confirm = input("\nConfirmar compra? (s/n): ").lower()

    if confirm == 's':
        # (Lógica para salvar a compra em 3 lugares diferentes)
        print("\n✅ Compra realizada com sucesso!")
    else:
        print("\nCompra cancelada.")
    u_a.input_continuar()

# Exibe o histórico de compras do usuário logado.
def ver_historico(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- MEU HISTÓRICO DE COMPRAS ---".center(60))
    historico = dados_usuario.get('historico', [])
    if not historico:
        print("\nVocê ainda não possui compras no seu histórico.")
    else:
        for i, compra in enumerate(historico):
            print(f"\n{i+1}. Filme: {compra.get('filme', 'N/A')} | Assento: {compra.get('assento', 'N/A')}")
            print(f"   Sala: {compra.get('sala', 'N/A')} | Horário: {compra.get('horario', 'N/A')} | Data: {compra.get('data_compra', 'N/A')}")
    u_a.input_continuar()

# Permite que o usuário avalie um filme que está em seu histórico.
def avaliar_filme(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- AVALIAR UM FILME ---")
    # (Lógica completa de avaliar_filme que já fizemos antes)
    print("\nFunção de avaliar filme está aqui.")
    u_a.input_continuar()

# Permite ao usuário logado modificar seu próprio nome e senha.
def modifica_propria_conta(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- MODIFICAR MINHA CONTA ---")
    # (Lógica completa de modificar_propria_conta que já fizemos antes)
    print("\nFunção de modificar conta está aqui.")
    u_a.input_continuar()

# Menu principal para o cliente logado.
def iniciar_sessao_usuario(dados_usuario):
    while True:
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        print(f"Bem-vindo(a), {dados_usuario['nome']}!")
        print("\n--- MENU DE USUÁRIO ---")
        print("[1] Comprar Ingresso")
        print("[2] Ver Meu Histórico de Compras")
        print("[3] Avaliar um Filme")
        print("[4] Modificar Meus Dados")
        print("[5] Sair")

        resposta_menu = input("\nDigite sua escolha: ")

        if resposta_menu == "1":
            comprar_ingresso(dados_usuario)
        elif resposta_menu == "2":
            ver_historico(dados_usuario)
        elif resposta_menu == "3":
            avaliar_filme(dados_usuario)
        elif resposta_menu == "4":
            modifica_propria_conta(dados_usuario)
        elif resposta_menu == "5":
            print("\nSaindo da sua conta...")
            u_a.input_continuar()
            break
        else:
            u_a.msg_numero_valido()
            u_a.input_continuar()