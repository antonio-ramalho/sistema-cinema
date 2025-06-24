import json
import os

#Função para carregar os livros do arquivo
def carregar_filmes(nome_arquivo='filmes.json'):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []

#Função para salvar os filmes no arquivo
def salvar_filmes(catalogo, nome_arquivo='filmes.json'):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(catalogo, arquivo, ensure_ascii=False, indent=4)

#Função para gerar IDs
def gerar_id(catalogo):
    if not catalogo:
        return 1
    else:
        maior_id = max(filme.get('ID', 0) for filme in catalogo)
        return maior_id + 1

#Função para cadastrar filmes
def cadastra_filme(catalogo):
    while True:
        nome_filme = input('Digite o nome do filme: ')
        genero = input('Digite o gênero do filme: ')
        
        while True:
            try:
                lancamento = int(input('Digite o ano de lançamento do filme: '))
                if 0 < lancamento <= 2025:
                    break
                else:
                    print('Ano de lançamento inválido! Por favor, tente novamente.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')

        while True:
            try:
                duracao = int(input('Digite a duração do filme (em minutos): '))
                if duracao > 0:
                    break
                else:
                    print('Valor de duração inválido! Por favor, tente novamente.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')

        filme = {
            'ID': gerar_id(catalogo),
            'nome': nome_filme,
            'genero': genero,
            'lancamento': lancamento,
            'duracao': duracao,
        }
        
        if filme in catalogo:
            print(f'O filme {nome_filme} já está cadastrado')
        else:
            catalogo.append(filme)
            print(f"\nFilme '{nome_filme}' cadastrado com sucesso!")
            
            salvar_filmes(catalogo)


        if input('Deseja cadastrar outro filme? (s/n) ').lower() == 'n':
            break

#Função para buscar os filmes com base no ID
def buscar_filme(catalogo, id_filme):
    for filme in catalogo:
        if filme.get('ID') == id_filme:
            return filme
    return None

def excluir_filme(catalogo):
    if not catalogo:
        print("O catálogo está vazio. Não há filmes para excluir.")
        return catalogo

    catalogo_em_edicao = list(catalogo)

    while True:
        print("\n--- Catálogo de Filmes Atual ---")
        mostrar_filmes(catalogo_em_edicao)
        print("--------------------------------")

        try:
            id_para_excluir = int(input("Digite o ID do filme que deseja excluir (ou digite 0 para sair): "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if id_para_excluir == 0:
            print("Operação de exclusão cancelada.")
            break

        filme_para_excluir = buscar_filme(catalogo_em_edicao, id_para_excluir)

        if filme_para_excluir:
            nome_do_filme = filme_para_excluir.get('nome', 'N/A')

            confirmacao = input(f"Tem certeza que deseja excluir o filme '{nome_do_filme}' (ID: {id_para_excluir})? (s/n): ").lower()

            if confirmacao == 's':
                catalogo_em_edicao.remove(filme_para_excluir)
                print(f"Filme '{nome_do_filme}' foi excluído com sucesso!")
                
                salvar_filmes(catalogo_em_edicao)
            else:
                print("Exclusão cancelada pelo usuário.")
        else:
            print(f"Filme com ID {id_para_excluir} não foi encontrado no catálogo.")

        # 5. Perguntar se deseja excluir outro filme
        if input("\nDeseja excluir outro filme? (s/n) ").lower() != 's':
            break
            
    return catalogo_em_edicao

#Função para mostrar o catálogo
def mostrar_filmes(catalogo):
    for filme in catalogo:
        print(' ')
        print(f'ID: {filme['ID']}')
        print(f'Nome: {filme['nome']}')
        print(f'Gênero: {filme['genero']}')
        print(f'Ano de Lançamento: {filme['lancamento']}')
        print(f'Duração: {((filme['duracao'])//60)}h {((filme['duracao'])%60)}min')
        print(' ')

#Função para escolher filme
def escolher_filme(catalogo):
    if not catalogo:
        print("O catálogo está vazio.")
        return None

    while True:
        mostrar_filmes(catalogo)
        try:
            filme_escolhido = int(input('Digite o ID do filme escolhido (ou 0 para cancelar): '))
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')
            continue

        if filme_escolhido == 0:
            return None 

        filme_encontrado = buscar_filme(catalogo, filme_escolhido)

        if filme_encontrado:
            print(f"\nFilme '{filme_encontrado.get('nome')}' selecionado com sucesso!")
            return filme_encontrado
        else:
            print(f'\nO filme com ID {filme_escolhido} não foi encontrado!')

        if input("Deseja tentar escolher outro filme? (s/n) ").lower() == 'n':
            break
    
    return None


#Variáveis
catalogo = carregar_filmes()

