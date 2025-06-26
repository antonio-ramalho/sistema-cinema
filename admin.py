import json
import os
import dados
import utils as u_a
import filmes
from collections import Counter
## ------------------------------------------------------------------------------------
## --------------- CADASTRA / MODIFICA / EXCLUI USUÁRIO -------------------------------
## ------------------------------------------------------------------------------------


SENHA_MESTRA_ADMIN = "adm123"
ARQUIVO_USUARIOS = "users_list.json"


def cadastrar_usuario(nome, cpf, senha, admin=False):
    usuarios = dados.carregar_usuarios()
    if cpf in usuarios:
        print(f" Erro: O CPF {cpf} já está cadastrado no sistema.")
        return
    usuarios[cpf] = {'nome': nome, 'senha': senha, 'admin': admin}
    dados.salvar_usuarios(usuarios)
    if admin:
        print(f"  Usuário '{nome}' cadastrado com sucesso como ADMINISTRADOR.")
    else:
        print(f"  Usuário '{nome}' cadastrado com sucesso.")

def modifica_usuario():
    usuarios = dados.carregar_usuarios()
    cpf = input("Digite o CPF do usuário que deseja modificar: ")
    if cpf not in usuarios:
        print(" Usuário não encontrado.")
        return
    print(f"Usuário atual: {usuarios[cpf]}")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    nova_senha = input("Digite a nova senha (ou pressione Enter para manter a atual): ")

    if novo_nome.strip():
        usuarios[cpf]['nome'] = novo_nome
    if nova_senha.strip():
        usuarios[cpf]['senha'] = nova_senha

    dados.salvar_usuarios(usuarios)
    print(" Dados do usuário atualizados com sucesso.")

def menu_cadastro():
    print("\n--- Tela de Cadastro de Novo Usuário ---")
    nome_input = input("Digite o nome do usuário: ")
    while True:
        cpf_input = input("Digite o CPF do usuário (somente números, 11 dígitos): ")
        if cpf_input.isdigit() and len(cpf_input) == 11:
            break
        else:
            print(" CPF inválido! Certifique-se de digitar exatamente 11 números.")
    senha_usuario = input(f"Crie uma senha para a conta de '{nome_input}': ")
    senha_mestra_input = input("Digite a senha mestra para tornar este usuário um ADM (ou pressione Enter para criar um usuário comum): ")

    admin = False
    if senha_mestra_input == SENHA_MESTRA_ADMIN:
        print(" Senha mestra correta! Privilégios de administrador concedidos.")
        admin = True
    elif senha_mestra_input != "":
        print(" Senha mestra incorreta. O usuário será criado como comum.")

    cadastrar_usuario(nome_input, cpf_input, senha_usuario, admin)

def exclui_usuario():
    usuarios = dados.carregar_usuarios()
    cpf = input("Digite o CPF do usuário que deseja excluir: ")
    if cpf in usuarios:
        confirm = input(f"Tem certeza que deseja excluir o usuário '{usuarios[cpf]['nome']}'? (s/n): ").lower()
        if confirm == 's':
            del usuarios[cpf]
            dados.salvar_usuarios(usuarios)
            print(" Usuário excluído com sucesso.")
        else:
            print(" Operação cancelada.")
    else:
        print(" Usuário não encontrado.")


## -----------------------------------------------------------------
## --------------------- LISTAR / LOGIN / PREÇO / RELATORIO ----------------------------
## -----------------------------------------------------------------


def listar_usuarios():
    usuarios = dados.carregar_usuarios()
    print("--- Lista de Usuários no Sistema ---".center(60))
    print("-" * 60)
    for cpf, usuario in usuarios.items():
        print(f"Nome do usuário: {usuario['nome']}")
        print(f"Cpf do(a) {usuario['nome']}: {cpf}")
        
        if 'historico' in usuario: 
            print(f"Número de compras recentes do {usuario['nome']}: {len(usuario['historico'])}")
        else:
            print(f"Número de compras recentes do {usuario['nome']}: Não fez nenhuma compra recente")
        
        if 'filmes_avaliados' in usuario: 
            print(f"Número de filmes avaliados: {usuario['filmes_avaliados']}")   
        else:
            print("Número de filmes avaliados: Ainda não avaliou nenhum filme")
        print("-" * 60)
        print(" ")      

def login():
    usuarios = dados.carregar_usuarios() 
    cpf_login = input("Digite o CPF do usuário: ")
    if cpf_login in usuarios:
        senha_login = input("Digite a senha do usuário: ")
        if usuarios[cpf_login]["senha"] == senha_login:
            nome = usuarios[cpf_login]["nome"]
            print(f"✅ Usuário {nome} (CPF: {cpf_login}), bem-vindo de volta!")
            return cpf_login
        else:
            print(" Senha incorreta!")
    else:
        print(" Usuário não encontrado.")

def definir_preco_filme():
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- DEFINIR PREÇO DE FILME ---".center(60))

    catalogo = dados.carregar_filmes() 
    if not catalogo:
        print("\nNão há filmes cadastrados.")
        u_a.input_continuar()
        return

    filmes.mostrar_filmes(catalogo)
    
    try:
        id_filme = int(input("\nDigite o ID do filme para alterar o preço (ou 0 para voltar): "))
        if id_filme == 0:
            return

        filme_encontrado = filmes.buscar_filme(catalogo, id_filme) 
        
        if not filme_encontrado:
            print(" Filme com este ID não encontrado.")
            u_a.input_continuar()
            return

        novo_preco_str = input(f"Digite o novo preço para '{filme_encontrado['nome']}' (ex: 35.50): ")
        novo_preco = float(novo_preco_str.replace(',', '.'))
        filme_encontrado['preco'] = novo_preco
        
        dados.salvar_filmes(catalogo)
        
        print(f"\n Preço atualizado para R$ {novo_preco:.2f}")

    except ValueError:
        print("\n Valor inválido. Por favor, digite um número.")
    
    u_a.input_continuar()

def mostrar_relatorios():
    u_a.limpar_console()
    u_a.cabecalho_cinemax()
    print("--- RELATÓRIOS ---".center(60))
    # Relatorio de avaliação
    print("\n" + " FILMES MELHOR AVALIADOS (TOP 5) ".center(60, "-"))
    filmes = dados.carregar_filmes()
    avaliacoes = dados.carregar_avaliacoes()
    
    filmes_com_media = []
    if not filmes:
        print("\nNenhum filme cadastrado.")
    elif not avaliacoes:
        print("\nAinda não há avaliações para classificar os filmes.")
    else:
        for filme in filmes:
            id_filme = str(filme.get('ID'))
            lista_de_notas = avaliacoes.get(id_filme, [])
            if lista_de_notas:
                media = sum(lista_de_notas) / len(lista_de_notas)
                filmes_com_media.append({'nome': filme['nome'], 'media': media, 'num_avaliacoes': len(lista_de_notas)})
        
        filmes_ordenados = sorted(filmes_com_media, key=lambda f: f['media'], reverse=True)
        
        if not filmes_ordenados:
            print("\nNenhum filme foi avaliado ainda.")
        else:
            for i, filme_info in enumerate(filmes_ordenados[:5]):
                print(f"{i+1}º: {filme_info['nome']} - Média: {filme_info['media']:.1f}/5.0 ({filme_info['num_avaliacoes']} votos)")
        # Relatorio de filmes
    print("\n" + " FILMES MAIS ASSISTIDOS (TOP 5) ".center(60, "-"))
    usuarios = dados.carregar_usuarios() 
    
    historico_geral = []
    for dados_usuario in usuarios.values():
        for compra in dados_usuario.get('historico', []):
            historico_geral.append(compra.get('filme'))
    

    historico_geral = [filme for filme in historico_geral if filme]

    if not historico_geral:
        print("\nNenhum ingresso foi comprado ainda.")
    else:
        contagem_filmes = Counter(historico_geral)
        
        for i, (filme, contagem) in enumerate(contagem_filmes.most_common(5)):
            print(f"{i+1}º: {filme} - {contagem} ingresso(s) vendido(s)")

    # 3.Relatório de ingressos

    print("\n" + " TOTAL DE INGRESSOS VENDIDOS ".center(60, "-"))
    bilhetes = dados.carregar_bilhetes()
    
    total_ingressos = sum(bilhete.get('quantidade', 0) for bilhete in bilhetes)
        
    print(f"\nTotal de ingressos vendidos no sistema: {total_ingressos}")
    
    print("-" * 60)
    u_a.input_continuar()
