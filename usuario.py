import dados
import utils as u_a

# --- FUNÇÕES AUXILIARES (usadas por outras funções, não aparecem no menu) ---

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

# --- Funções do Menu do Cliente ---

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
        usuarios = dados.carregar_usuarios()
        if 'historico' not in usuarios[dados_usuario['cpf']]: usuarios[dados_usuario['cpf']]['historico'] = []
        compra = {"filme": filme_selecionado['nome'], "data_compra": "25/06/2025", "sala": sessao_selecionada['sala_sessao'], "horario": sessao_selecionada['horario_inicio'], "assento": assento_escolhido}
        usuarios[dados_usuario['cpf']]['historico'].append(compra)
        dados.salvar_usuarios(usuarios)

        salas = dados.carregar_salas()
        for s in salas:
            for sess in s.get('sessoes_associadas', []):
                if sess.get('id_sessao') == sessao_selecionada.get('id_sessao') and sess.get('id_sala') == sessao_selecionada.get('id_sala'):
                    if 'assentos_ocupados' not in sess: sess['assentos_ocupados'] = []
                    sess['assentos_ocupados'].append(assento_escolhido)
                    break
        dados.salvar_salas(salas)

        bilhetes = dados.carregar_bilhetes()
        novo_bilhete = { "cpf": dados_usuario['cpf'], "filme": filme_selecionado['nome'], "quantidade": 1, "preco": 30.00 }
        bilhetes.append(novo_bilhete)
        dados.salvar_bilhetes(bilhetes)
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
    print("--- AVALIAR UM FILME ---".center(60))
    historico = dados_usuario.get('historico', [])
    if not historico:
        print("\nVocê precisa ter comprado um ingresso antes de poder avaliar um filme.")
        u_a.input_continuar()
        return

    filmes_no_historico = sorted(list(set(compra['filme'] for compra in historico)))
    for i, nome_filme in enumerate(filmes_no_historico):
        print(f"[{i+1}] - {nome_filme}")

    try:
        escolha = int(input("\nEscolha um filme para avaliar (ou 0 para voltar): "))
        if escolha == 0: return
        nome_filme_escolhido = filmes_no_historico[escolha - 1]
        
        catalogo_filmes = dados.carregar_filmes()
        filme_obj = next((f for f in catalogo_filmes if f['nome'] == nome_filme_escolhido), None)
        if not filme_obj or 'ID' not in filme_obj:
            print("Erro: Filme não encontrado no catálogo principal.")
            u_a.input_continuar()
            return

        id_filme = str(filme_obj['ID'])
        filmes_ja_avaliados = dados_usuario.get('filmes_avaliados', [])
        if int(id_filme) in filmes_ja_avaliados:
            print("\n❌ Você já avaliou este filme.")
            u_a.input_continuar()
            return

        nota = int(input(f"Qual nota de 1 a 5 para '{nome_filme_escolhido}'? "))
        if not 1 <= nota <= 5: raise ValueError("Nota fora do intervalo")

        avaliacoes = dados.carregar_avaliacoes()
        lista_de_notas = avaliacoes.get(id_filme, [])
        lista_de_notas.append(nota)
        avaliacoes[id_filme] = lista_de_notas
        dados.salvar_avaliacoes(avaliacoes)

        usuarios = dados.carregar_usuarios()
        if 'filmes_avaliados' not in usuarios[dados_usuario['cpf']]:
            usuarios[dados_usuario['cpf']]['filmes_avaliados'] = []
        usuarios[dados_usuario['cpf']]['filmes_avaliados'].append(int(id_filme))
        dados.salvar_usuarios(usuarios)
        
        print("\n✅ Obrigado! Sua nota foi registrada.")
    except (ValueError, IndexError):
        print("\nOpção inválida.")
    u_a.input_continuar()

# Permite ao usuário logado modificar seu próprio nome e senha.
def modifica_propria_conta(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- MODIFICAR MINHA CONTA ---".center(60))
    cpf_logado = dados_usuario['cpf']
    usuarios = dados.carregar_usuarios()
    print(f"Nome atual: {usuarios[cpf_logado]['nome']}")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ").strip()
    nova_senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ").strip()

    if novo_nome: usuarios[cpf_logado]['nome'] = novo_nome
    if nova_senha: usuarios[cpf_logado]['senha'] = nova_senha
    
    dados.salvar_usuarios(usuarios)
    print("\nSuas informações foram salvas.")
    u_a.input_continuar()
