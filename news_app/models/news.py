class News:
    """
    Classe que representa uma notícia.
    Esta classe armazena as informações básicas de uma notícia,
    incluindo o título, a descrição e o tipo da notícia.
    """
    
    def __init__(self, title, description, news_type):
        """
        Método construtor da classe News.
        Inicializa os atributos da notícia com os valores fornecidos.

        :param title: Título da notícia.
        :param description: Descrição da notícia.
        :param news_type: Tipo ou categoria da notícia.
        """
        self.title = title  # Inicializa o atributo 'title' com o título da notícia
        self.description = description  # Inicializa o atributo 'description' com a descrição da notícia
        self.news_type = news_type  # Inicializa o atributo 'news_type' com o tipo da notícia
