from app import app
# Importa a instância do aplicativo Flask configurada no módulo 'app'

if __name__ == "__main__":
    """
    Verifica se o script está sendo executado diretamente.
    Se verdadeiro, inicia o servidor Flask.
    """
    app.run(debug=True)
    # Inicia o servidor com o modo de depuração ativado.
    # O modo de depuração permite recarregar automaticamente o servidor em caso de alterações no código
    # e exibe mensagens detalhadas de erro em caso de falhas.
