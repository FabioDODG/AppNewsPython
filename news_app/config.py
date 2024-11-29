import os

class Config:
    """
    Classe de configuração para a aplicação Flask.
    Define configurações básicas como chave secreta e modo de depuração.
    """

    # Define a chave secreta para proteger sessões e outros dados sensíveis
    # Busca do ambiente do sistema ou usa um valor padrão
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_default'

    # Habilita o modo de depuração, útil para desenvolvimento
    DEBUG = True
