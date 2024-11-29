import json

def load_news():
    """
    Carrega as notícias de um arquivo JSON.
    Retorna uma lista de notícias ou uma lista vazia se o arquivo não existir.
    """
    try:
        # Tenta abrir o arquivo 'news.json' no modo de leitura
        with open('news.json', 'r') as f:
            news = json.load(f)  # Carrega os dados do arquivo JSON em uma lista
    except FileNotFoundError:
        # Caso o arquivo não exista, retorna uma lista vazia
        news = []
    return news  # Retorna a lista de notícias

def save_news(news_list):
    """
    Salva uma lista de notícias em um arquivo JSON.
    Sobrescreve os dados existentes no arquivo.
    """
    with open('news.json', 'w') as f:
        # Salva a lista de notícias no arquivo 'news.json'
        # Usa json.dump para converter a lista em formato JSON
        json.dump(news_list, f)

def save_news_type(news_type):
    """
    Adiciona um tipo de notícia à lista de tipos no arquivo JSON.
    Evita duplicatas e cria o arquivo se ele não existir.
    """
    try:
        # Tenta abrir o arquivo 'news_types.json' no modo de leitura
        with open('news_types.json', 'r') as f:
            news_types = json.load(f)  # Carrega os tipos de notícias existentes
    except FileNotFoundError:
        # Caso o arquivo não exista, inicia uma lista vazia
        news_types = []

    # Adiciona o novo tipo à lista apenas se ele não existir
    if news_type not in news_types:
        news_types.append(news_type)

    with open('news_types.json', 'w') as f:
        # Salva a lista atualizada de tipos no arquivo 'news_types.json'
        json.dump(news_types, f)
