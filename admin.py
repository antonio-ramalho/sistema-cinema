import json
import os

SENHA_MESTRA_ADMIN = "adm123"
ARQUIVO_USUARIOS = "users_list.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
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
        else:
            print("❌ Senha incorreta!")
    else:
        print("❌ Usuário não encontrado.")

# Execução de testes

login()
menu_cadastro()
menu_cadastro()
menu_cadastro()
listar_usuarios()
modifica_usuario()
listar_usuarios()


##login()

##define_preço() 

##gera_relatorio() 

##filme mais bem votado 
##renda por sala 
##filmes com mais pessoas 
##filmes mais lurativos 
##etc. 

##cancela_bilhete() 

##exclui_usuario() 
