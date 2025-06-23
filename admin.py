import json
import os

## ------------------------------------------------------------------------------------
## --------------- CADASTRA / MODIFICA / EXCLUI USUÁRIO -------------------------------
## ------------------------------------------------------------------------------------


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

def exclui_usuario():
    usuarios = carregar_usuarios()
    cpf = input("Digite o CPF do usuário que deseja excluir: ")
    if cpf in usuarios:
        confirm = input(f"Tem certeza que deseja excluir o usuário '{usuarios[cpf]['nome']}'? (s/n): ").lower()
        if confirm == 's':
            del usuarios[cpf]
            salvar_usuarios(usuarios)
            print("✅ Usuário excluído com sucesso.")
        else:
            print("❌ Operação cancelada.")
    else:
        print("❌ Usuário não encontrado.")

## -----------------------------------------------------------------
## --------------------- LISTAR / LOGIN ----------------------------
## -----------------------------------------------------------------


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

## ----------------------------------------------------------------------------
## ---------------------- CANCELA / GERA RELATORIO ----------------------------
## ----------------------------------------------------------------------------

def gera_relatorio():
    ARQUIVO_BILHETES = "bilhetes.json"
    ARQUIVO_RELATORIO = "relatorio_vendas.json"

    if not os.path.exists(ARQUIVO_BILHETES):
        with open(ARQUIVO_BILHETES, "w") as f:
            json.dump([], f)
        print(f"⚠️ Arquivo '{ARQUIVO_BILHETES}' não existia e foi criado vazio.")
        print("ℹ Nenhum dado disponível para gerar relatório.")
        return

    with open(ARQUIVO_BILHETES, "r") as f:
        bilhetes = json.load(f)

    if not bilhetes:
        print("ℹ Nenhum bilhete registrado. Relatório não gerado.")
        return

    total_bilhetes = 0
    total_receita = 0.0
    publico_filme = {}
    receita_filme = {}

    for b in bilhetes:
        filme = b["filme"]
        qtd = b["quantidade"]
        preco = b["preco"]
        total_bilhetes += qtd
        total_receita += qtd * preco

        publico_filme[filme] = publico_filme.get(filme, 0) + qtd
        receita_filme[filme] = receita_filme.get(filme, 0.0) + qtd * preco

    relatorio = {
        "total_bilhetes_vendidos": total_bilhetes,
        "receita_total": round(total_receita, 2),
        "publico_por_filme": publico_filme,
        "receita_por_filme": {f: round(v, 2) for f, v in receita_filme.items()}
    }

    with open(ARQUIVO_RELATORIO, "w") as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)

    print(f" Relatório gerado com sucesso em '{ARQUIVO_RELATORIO}'.")
    print(f" Total de bilhetes: {total_bilhetes} |  Receita total: R$ {total_receita:.2f}")


def cancela_bilhete():
    try:
        with open("bilhetes.json", "r") as f:
            bilhetes = json.load(f)
    except FileNotFoundError:
        print("❌ Nenhuma venda registrada.")
        return

    cpf = input("Digite o CPF para o qual deseja cancelar um bilhete: ")
    bilhetes_filtrados = [b for b in bilhetes if b["cpf"] != cpf]

    if len(bilhetes) == len(bilhetes_filtrados):
        print("⚠️ Nenhum bilhete encontrado para este CPF.")
        return

    with open("bilhetes.json", "w") as f:
        json.dump(bilhetes_filtrados, f, indent=2)

    print(f"✅ Bilhetes do CPF {cpf} foram cancelados com sucesso.")


## ----------------------------------------------------------------------------
## ------------------------- EXECUCAO DE TESTES -------------------------------
## ----------------------------------------------------------------------------

##gera_relatorio()
##menu_cadastro()
##login()
##modifica_usuario()
##exclui_usuario()


##----------------------------------------------------------------------------------
##----------------------------------------------------------------------------------

##gera_relatorio() 

##filme mais bem votado ## Breno vai fazer a função de votar
##renda por sala ## Baseado no número de vendas de ingresso/bilhete
##filmes com mais pessoas ## Baseado no número de vendas de ingresso/bilhete
##filmes mais lucrativos ## Baseado no número de vendas de ingresso/bilhete

##----------------------------------------------------------------------------------
##----------------------------------------------------------------------------------
