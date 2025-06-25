
import json
import os

ARQUIVO_USUARIOS = "users_list.json"
ARQUIVO_FILMES = "filmes.json"
ARQUIVO_SALAS = "salas.json"
ARQUIVO_AVALIACOES = "avaliacoes.json"
ARQUIVO_BILHETES = "bilhetes.json"



def _carregar_json(caminho_arquivo, padrao_lista=False):
    """Função genérica e segura para carregar qualquer arquivo JSON."""
    if not os.path.exists(caminho_arquivo):
        return [] if padrao_lista else {}
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError):
        return [] if padrao_lista else {}

def _salvar_json(caminho_arquivo, dados):
    """Função genérica para salvar dados em qualquer arquivo JSON."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def carregar_usuarios():
    return _carregar_json(ARQUIVO_USUARIOS)

def salvar_usuarios(lista_de_usuarios):
    _salvar_json(ARQUIVO_USUARIOS, lista_de_usuarios)

def carregar_filmes():
    return _carregar_json(ARQUIVO_FILMES, padrao_lista=True)

def salvar_filmes(lista_de_filmes):
    _salvar_json(ARQUIVO_FILMES, lista_de_filmes)

def carregar_salas():
    return _carregar_json(ARQUIVO_SALAS, padrao_lista=True)

def salvar_salas(lista_de_salas):
    _salvar_json(ARQUIVO_SALAS, lista_de_salas)

def carregar_avaliacoes():
    return _carregar_json(ARQUIVO_AVALIACOES)

def salvar_avaliacoes(lista_de_avaliacoes):
    _salvar_json(ARQUIVO_AVALIACOES, lista_de_avaliacoes)

def carregar_bilhetes():
    return _carregar_json(ARQUIVO_BILHETES, padrao_lista=True)

def salvar_bilhetes(lista_de_bilhetes):
    _salvar_json(ARQUIVO_BILHETES, lista_de_bilhetes)