import json
import os
import filmes
import utils_armazenamento as u_a
import uuid


SENHA_MESTRA_ADMIN = "adm123"
ARQUIVO_USUARIOS = "users_list.json"

def carregar_avaliacoes():
    """Carrega os dados do arquivo de avaliações."""
    # Se o arquivo não existir ou estiver vazio, retorna um dicionário vazio.
    try:
        with open('avaliacoes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_avaliacoes(dados):
    """Salva os dados no arquivo de avaliações."""
    with open('avaliacoes.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding='utf-8-sig') as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=2)

def cadastrar_usuario(nome, cpf, senha, admin=False):
    usuarios = carregar_usuarios()
    if cpf in usuarios:
        print(f"⚠️  Erro: O CPF {cpf} já está cadastrado no sistema.")
        return
    usuarios[cpf] = {'nome': nome, 'senha': senha, 'admin': admin}
    salvar_usuarios(usuarios)
    if admin:
        print(f"✅  Usuário '{nome}' cadastrado com sucesso como ADMINISTRADOR.")
    else:
        print(f"✅  Usuário '{nome}' cadastrado com sucesso.")

def modifica_usuario():
    usuarios = carregar_usuarios()
    cpf = input("Digite o CPF do usuário que deseja modificar: ")
    if cpf not in usuarios:
        print("❌ Usuário não encontrado.")
        return
    print(f"Usuário atual: {usuarios[cpf]}")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    nova_senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ")

    if novo_nome.strip():
        usuarios[cpf]['nome'] = novo_nome
    if nova_senha.strip():
        usuarios[cpf]['senha'] = nova_senha

    salvar_usuarios(usuarios)
    print("✅ Dados do usuário atualizados com sucesso.")

def menu_cadastro():
    print("\n--- Tela de Cadastro de Novo Usuário ---")
    nome_input = input("Digite o nome do usuário: ")
    while True:
        cpf_input = input("Digite o CPF do usuário (somente números, 11 dígitos): ")
        if cpf_input.isdigit() and len(cpf_input) == 11:
            break
        else:
            print("❌ CPF inválido! Certifique-se de digitar exatamente 11 números.")
    senha_usuario = input(f"Crie uma senha para a conta de '{nome_input}': ")
    senha_mestra_input = input("Digite a senha mestra para tornar este usuário um ADM (ou pressione Enter para criar um usuário comum): ")

    admin = False
    if senha_mestra_input == SENHA_MESTRA_ADMIN:
        print(" Senha mestra correta! Privilégios de administrador concedidos.")
        admin = True
    elif senha_mestra_input != "":
        print(" Senha mestra incorreta. O usuário será criado como comum.")

    cadastrar_usuario(nome_input, cpf_input, senha_usuario, admin)

def listar_usuarios():
    usuarios = carregar_usuarios()
    print("\n--- Lista de Usuários no Sistema ---")
    for cpf, dados in usuarios.items():
        print(f"CPF: {cpf}, Dados: {dados}")

def login():
    usuarios = carregar_usuarios()
    cpf_login = input("Digite o CPF do usuário: ")

    if cpf_login in usuarios:
        senha_login = input("Digite a senha do usuário: ")
        if usuarios[cpf_login]["senha"] == senha_login:
            nome = usuarios[cpf_login]["nome"]
            print(f"✅ Usuário {nome} (CPF: {cpf_login}), bem-vindo de volta!")
            dados_usuario_logado = usuarios[cpf_login]
            dados_usuario_logado['cpf'] = cpf_login
            return dados_usuario_logado
        else:
            print("❌ Senha incorreta!")
            return None
    else:
        print("❌ Usuário não encontrado.")
        return None

def Modifica_propria_conta(usuario_logado_dados):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- MODIFICAR MINHA CONTA ---".center(60))

    if not usuario_logado_dados or 'cpf' not in usuario_logado_dados:
        print("Nenhum usuário logado ou dados incompletos. Não é possível modificar a conta.")
        u_a.input_continuar()
        return

    cpf_usuario_logado = usuario_logado_dados['cpf']

    usuarios = carregar_usuarios()

    if cpf_usuario_logado not in usuarios:
        print("Erro: Seus dados não foram encontrados no sistema. Tente logar novamente.")
        u_a.input_continuar()
        return

    print(f"Dados atuais da sua conta (CPF: {cpf_usuario_logado}):")
    print(f"Nome atual: {usuarios[cpf_usuario_logado]['nome']}")

    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ").strip()
    nova_senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ").strip()

    if novo_nome:
        usuarios[cpf_usuario_logado]['nome'] = novo_nome
        print("✅ Nome atualizado com sucesso!")
    else:
        print("Nome mantido como o atual.")

    if nova_senha:
        usuarios[cpf_usuario_logado]['senha'] = nova_senha # Corrigido: era 'cpf_logado'
        print("✅ Senha atualizada com sucesso!")
    else:
        print("Senha mantida como a atual.")

    salvar_usuarios(usuarios)
    print("Suas informações foram salvas.")
    u_a.input_continuar()


    usuarios = carregar_usuarios()
    cpf = input("Digite o CPF do usuário que deseja modificar: ")
    if cpf not in usuarios:
        print("❌ Usuário não encontrado.")
        return
    print(f"Usuário atual: {usuarios[cpf]}")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    nova_senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ")

    if novo_nome.strip():
        usuarios[cpf]['nome'] = novo_nome
    if nova_senha.strip():
        usuarios[cpf]['senha'] = nova_senha

    salvar_usuarios(usuarios)
    print("✅ Dados do usuário atualizados com sucesso.")

def _escolher_filme(catalogo):
    if not catalogo:
        print("Nenhum filme disponível para escolha.")
        input("Pressione Enter para continuar...")
        return None 
    
    print("\n--- Filmes Disponíveis para Escolha ---")

    for i, filme in enumerate(catalogo):
        print(f"[{i+1}] {filme['nome']} (Gênero: {filme['genero']})")

    while True:
        try:
            escolha_filme_idx = int(input("Digite o NÚMERO do filme desejado (ou 0 para voltar): ")) - 1

            if escolha_filme_idx == -1:
                print("Voltando à tela anterior.")
                input("Pressione Enter para continuar...")
                return None

            if 0 <= escolha_filme_idx < len(catalogo):
                filme_selecionado = catalogo[escolha_filme_idx]
                print(f"Você escolheu: {filme_selecionado['nome']}")
                return filme_selecionado
            else:
                print("Número de filme inválido. Por favor, digite um número da lista.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 0 para voltar.")
        input("Pressione Enter para continuar...")

    
    """
    Exibe o menu para um usuário que já está logado.
    Recebe os dados do usuário logado.
    """
    while True:
        u_a.limpar_console()
        u_a.cabecalho_cinemax()
        print(f"Bem-vindo(a), {dados_do_usuario['nome']}! (Logado como {'Admin' if dados_do_usuario.get('admin') else 'Comum'})")
        print("\n--- MENU DE USUÁRIO ---")

        menu_opcoes = ["[1] Filmes em cartaz", "[2] Modificar Meus Dados", "[3] Comprar Ingresso", "[4] Logout"]
        
        # Opções adicionais para administradores
        if dados_do_usuario.get('admin'):
            menu_opcoes.insert(2, "[X] Gerenciamento Admin") # Adicionei X como placeholder, defina um número real

        for item in menu_opcoes:
            print(item)
        resposta_menu_logado = input("Digite sua escolha: ")
        u_a.limpar_console()

        if resposta_menu_logado == "1": # Filmes em cartaz
            u_a.cabecalho_cinemax()
            filmes.mostrar_filmes(filmes.catalogo) # Assumindo que filmes.catalogo é global em filmes.py
            # Ou passe catalogo_filmes_global se você o define em menu_principal.py
        
        elif resposta_menu_logado == "2": # Modificar Meus Dados
            modulo_usuario.Modifica_propria_conta(dados_do_usuario) # PASSA os dados

        elif resposta_menu_logado == "3": # Comprar Ingresso
            # Chame sua função de compra de ingresso aqui.
            # Se a função de compra precisar dos dados do usuário, passe-os também.
            print("Função de compra de ingresso (com usuário logado).")
            # Exemplo: comprar_ingresso_real(dados_do_usuario)
            u_a.input_continuar()

        elif resposta_menu_logado == "4": # Logout
            print("Logout realizado com sucesso!")
            u_a.input_continuar()
            break

def pagamento_com_pix_simulado(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- PAGAMENTO VIA PIX ---")

    filme_simulado = {"nome": "Filme de Teste"}
    preco_simulado = 30.00

    chave_pix_simulada = str(uuid.uuid4())
    
    print("\nPara concluir sua compra, pague o valor abaixo usando a chave PIX.")
    print(f"Valor: R$ {preco_simulado:.2f}")
    print("\nChave PIX (Copia e Cola):")
    print(chave_pix_simulada)
    
    input("\n--> Após realizar o pagamento, pressione ENTER para confirmar e liberar seu ingresso...")

    usuarios = carregar_usuarios()
    cpf_logado = dados_usuario['cpf']

    if 'historico' not in usuarios[cpf_logado]:
        usuarios[cpf_logado]['historico'] = []

    compra = {"filme": filme_simulado['nome'], "data_compra": "23/06/2025"}
    usuarios[cpf_logado]['historico'].append(compra)
    salvar_usuarios(usuarios)

    print("\n✅ Pagamento confirmado! Seu ingresso foi liberado e a compra está no seu histórico.")
    u_a.input_continuar()

def iniciar_sessao_usuario():
    dados_usuario = login()
    if dados_usuario:
        while True:
            u_a.limpar_console()
            u_a.cabecalho_cinemax()
            print(f"Bem-vindo(a), {dados_usuario['nome']}!")
            print("\n--- MENU DE USUÁRIO ---")

            print("[1] Comprar Ingresso")
            print("[2] Ver Meu Histórico de Compras")
            print("[3] Avaliar um Filme")
            print("[4] Modificar Meus Dados")
            print("[5] Logout")
            
            resposta_menu = input("\nDigite sua escolha: ")

            if resposta_menu == "1":
                _escolher_filme(filmes.catalogo)
                pagamento_com_pix_simulado(dados_usuario)
                u_a.input_continuar()
            
            elif resposta_menu == "2":
                ver_historico(dados_usuario)
                u_a.input_continuar()

            elif resposta_menu == "3":
                avaliar_filme(dados_usuario)
                u_a.input_continuar()

            elif resposta_menu == "4":
           
                Modifica_propria_conta(dados_usuario)
            
            elif resposta_menu == "5":
                print("\nLogout realizado com sucesso!")
                u_a.input_continuar()
                break
    else:
        print("\nFalha no login.")
        u_a.input_continuar()

def ver_historico(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- MEU HISTÓRICO DE COMPRAS ---".center(60))

    historico_de_compras = dados_usuario.get('historico', [])

    if not historico_de_compras:
        print("\nVocê ainda não possui compras no seu histórico.")
    else:
        print("\nEstes são os ingressos que você já comprou:\n")
        for i, compra in enumerate(historico_de_compras):
    
            print(f"  {i+1}. Filme: {compra.get('filme', 'N/A')}")
            print(f"     Data da Compra: {compra.get('data_compra', 'N/A')}")
            print("-" * 40)

    u_a.input_continuar()


    """Salva os dados no arquivo de avaliações."""
    with open('avaliacoes.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def avaliar_filme(dados_usuario):
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- AVALIAR UM FILME ---".center(60))

    historico = dados_usuario.get('historico', [])
    if not historico:
        print("\nVocê precisa ter comprado um ingresso antes de poder avaliar um filme.")
        u_a.input_continuar()
        return

    print("\nEscolha um filme do seu histórico para avaliar:\n")
    filmes_no_historico = list(set(compra['filme'] for compra in historico))
    
    for i, nome_filme in enumerate(filmes_no_historico):
        print(f"  [{i+1}] - {nome_filme}")

    try:
        escolha = int(input("\nDigite o número do filme (ou 0 para voltar): "))
        if escolha == 0: return
        
        nome_filme_escolhido = filmes_no_historico[escolha - 1]

        catalogo_filmes = filmes.carregar_filmes()
        filme_obj = next((f for f in catalogo_filmes if f['nome'] == nome_filme_escolhido), None)
        
        if not filme_obj or 'id' not in filme_obj:
            print("Erro: Não foi possível encontrar o ID do filme selecionado.")
            u_a.input_continuar()
            return
            
        id_filme = str(filme_obj['id'])

        filmes_ja_avaliados = dados_usuario.get('filmes_avaliados', [])
        if int(id_filme) in filmes_ja_avaliados:
            print("\n❌ Você já avaliou este filme anteriormente.")
            u_a.input_continuar()
            return

        while True:
            try:
                nota = int(input(f"\nQual nota de 1 a 5 você dá para '{nome_filme_escolhido}'? "))
                if 1 <= nota <= 5: break
                else: print("Por favor, digite uma nota entre 1 e 5.")
            except ValueError: print("Entrada inválida. Por favor, digite um número.")

        avaliacoes = carregar_avaliacoes()
        lista_de_notas = avaliacoes.get(id_filme, [])
        lista_de_notas.append(nota)
        avaliacoes[id_filme] = lista_de_notas
        salvar_avaliacoes(avaliacoes)

        usuarios = carregar_usuarios()
        cpf_logado = dados_usuario['cpf']
        if 'filmes_avaliados' not in usuarios[cpf_logado]:
            usuarios[cpf_logado]['filmes_avaliados'] = []
        usuarios[cpf_logado]['filmes_avaliados'].append(int(id_filme))
        salvar_usuarios(usuarios)

        print(f"\n✅ Obrigado! Sua nota {nota} para o filme '{nome_filme_escolhido}' foi registrada.")

    except (ValueError, IndexError):
        print("\nOpção inválida.")

    u_a.input_continuar()
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- AVALIAR UM FILME ---".center(60))

    historico = dados_usuario.get('historico', [])

    if not historico:
        print("\nVocê precisa ter comprado um ingresso antes de poder avaliar um filme.")
        u_a.input_continuar()
        return

    print("\nEscolha um filme do seu histórico para avaliar:\n")
    
    filmes_unicos = list(set(compra['filme'] for compra in historico))
    
    for i, nome_filme in enumerate(filmes_unicos):
        print(f"  [{i+1}] - {nome_filme}")

    try:
        escolha = int(input("\nDigite o número do filme (ou 0 para voltar): "))
        if escolha == 0:
            return
        
        filme_escolhido = filmes_unicos[escolha - 1]

        while True:
            try:
                nota = int(input(f"\nQual nota de 1 a 5 você dá para '{filme_escolhido}'? "))
                if 1 <= nota <= 5:
                    break
                else:
                    print("Por favor, digite uma nota entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        print(f"\n✅ Obrigado! Sua nota {nota} para o filme '{filme_escolhido}' foi registrada (simulação).")

    except (ValueError, IndexError):
        print("\nOpção inválida.")

    u_a.input_continuar()

iniciar_sessao_usuario()
