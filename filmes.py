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
                duracao = int(input('Digite a duração do filme (em minutos) '))
                if duracao > 0:
                    break
                else:
                    print('Valor de duração inválido!Por favor, tente novamente.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')

        filme = {
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

#Função para excluir filmes do catálogo
def excluir_filme(catalogo):
    if not catalogo:
        print("O catálogo está vazio. Não há filmes para excluir.")
        return catalogo
    
    nome_para_excluir = input("Digite o nome do filme que deseja excluir: ")
    catalogo_atualizado = [filme for filme in catalogo if filme['nome'].lower() != nome_para_excluir.lower()]

    if len(catalogo_atualizado) < len(catalogo):
        salvar_filmes(catalogo_atualizado)
        print(f"Filme '{nome_para_excluir}' foi excluído com sucesso!")
        return catalogo_atualizado
    else:
        print(f"Filme '{nome_para_excluir}' não encontrado no catálogo.")
        return catalogo

#Função para mostrar o catálogo
def mostrar_filmes(catalogo):
    for filme in catalogo:
        print(' ')
        print(f'Nome: {filme['nome']}')
        print(f'Gênero: {filme['genero']}')
        print(f'Ano de Lançamento: {filme['lancamento']}')
        print(f'Duração: {((filme['duracao'])//60)}h {((filme['duracao'])%60)}min')
        print(' ')



#Variáveis
catalogo = carregar_filmes()
