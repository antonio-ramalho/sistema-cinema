# --- CONFIGURAÇÃO ---
SENHA_MESTRA_ADMIN = "adm123"

# Dicionário para simular nosso banco de dados
usuarios = {}

def cadastrar_usuario(nome, cpf, senha, admin=False):
  """
  Responsabilidade ÚNICA: Cadastrar um novo usuário se o CPF não existir.
  """
  # Se o CPF já existe no dicionário, avisa o erro e para.
  if cpf in usuarios:
    print(f"⚠️  Erro: O CPF {cpf} já está cadastrado no sistema.")
    return

  # Se o CPF é novo, cria o registro do usuário.
  usuarios[cpf] = {
      'nome' : nome,
      'senha': senha,
      'admin': admin
  }

  if admin:
    print(f"✅  Usuário '{nome}' cadastrado com sucesso como ADMINISTRADOR.")
  else:
    print(f"✅  Usuário '{nome}' cadastrado com sucesso.")

def menu_cadastro():
  """
  Pede os dados ao usuário e chama a função de cadastro.
  """
  print("\n--- Tela de Cadastro de Novo Usuário ---")
  
  nome_input = input("Digite o nome do usuário: ")
  cpf_input = input("Digite o CPF do usuário: ")
  
  #Pede a senha para a conta do novo usuário.
  senha_usuario = input(f"Crie uma senha para a conta de '{nome_input}': ")

  #Pede a senha mestra para tentar dar o privilégio de adm.
  senha_mestra_input = input("Digite a senha mestra para tornar este usuário um ADM (ou pressione Enter para criar um usuário comum): ")

  # Verifica se a senha mestra foi digitada corretamente
  admin = False
  if senha_mestra_input == SENHA_MESTRA_ADMIN:
    print("✨ Senha mestra correta! Privilégios de administrador concedidos.")
    admin = True
  elif senha_mestra_input != "":
    print("❌ Senha mestra incorreta. O usuário será criado como comum.")

  # Chama a função de cadastro passando os dados corretos:
  # A senha do usuário é a 'senha_usuario', não a senha mestra.
  cadastrar_usuario(nome_input, cpf_input, senha_usuario, admin)


menu_cadastro()

menu_cadastro()

menu_cadastro()

# --- Verificando o resultado final ---
print("\n--- Lista de Usuários no Sistema ---")
# Imprime de uma forma mais legível
for cpf, dados in usuarios.items():
    print(f"CPF: {cpf}, Dados: {dados}")

##modifica_usuario() 

##define_preço() 

##gera_relatorio() 

##filme mais bem votado 
##renda por sala 
##filmes com mais pessoas 
##filmes mais lurativos 
##etc. 

##cancela_bilhete() 

##exclui_usuario() 