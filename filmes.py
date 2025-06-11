import menu_principal

filmes = []

def cadastra_filme():
    while True:
        nome_filme = input('Digite o nome do filme: ')
        genero = input('Digite o gênero do filme: ')
        lancamento = input('Digite o ano de lançamento do filme: ')
        
