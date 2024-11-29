from flask import Flask, render_template, request, redirect, url_for
from utils import load_news, save_news, save_news_type
import json

app = Flask(__name__)

# Carregar as notícias do arquivo JSON ao iniciar o aplicativo
news_list = load_news()

@app.route('/')
def index():
    query = request.args.get('query')
    if query:
        # Filtra as notícias pelo título ou pela categoria
        filtered_news = [
            news for news in news_list 
            if query.lower() in news['title'].lower() or query.lower() in news['type'].lower()
        ]
    else:
        filtered_news = news_list
    return render_template('index.html', news=enumerate(filtered_news))

@app.route('/type_news', methods=['GET', 'POST'])
def type_news():
    # Carregar os tipos de notícias do arquivo JSON
    try:
        with open('news_types.json', 'r') as f:
            news_types = json.load(f)
    except FileNotFoundError:
        news_types = []  # Se o arquivo não existe, inicia uma lista vazia

    if request.method == 'POST':
        new_type = request.form.get('new_type')
        # Verifica se o tipo já existe para evitar duplicatas
        if new_type and new_type not in news_types:
            news_types.append(new_type)  # Adiciona o novo tipo à lista
            # Salva a lista atualizada no arquivo JSON
            with open('news_types.json', 'w') as f:
                json.dump(news_types, f)
        return redirect(url_for('type_news'))

    return render_template('type_news.html', news_types=news_types)

@app.route('/remove_news_type', methods=['POST'])
def remove_news_type():
    type_to_remove = request.form.get('news_type')
    
    # Carrega os tipos existentes
    try:
        with open('news_types.json', 'r') as f:
            news_types = json.load(f)
    except FileNotFoundError:
        news_types = []  # Se o arquivo não existe, inicia uma lista vazia

    # Remove o tipo, se existir
    if type_to_remove in news_types:
        news_types.remove(type_to_remove)

    # Salva a lista atualizada
    with open('news_types.json', 'w') as f:
        json.dump(news_types, f)

    return redirect(url_for('type_news'))

@app.route('/news/<int:news_id>')
def news_detail(news_id):
    if 0 <= news_id < len(news_list):
        news_item = news_list[news_id]
        return render_template('news_detail.html', news=news_item, news_id=news_id)
    return redirect(url_for('index'))

@app.route('/edit_news/<int:news_id>', methods=['GET', 'POST'])
def edit_news(news_id):
    if 0 <= news_id < len(news_list):
        news_item = news_list[news_id]

        if request.method == 'POST':
            # Atualiza os dados da notícia com os novos valores do formulário
            news_item['title'] = request.form['title']
            news_item['description'] = request.form['description']
            news_item['type'] = request.form['news_type']  # Mudado para 'news_type' para corresponder ao seu formulário
            # Salvar a lista atualizada no arquivo JSON
            save_news(news_list)
            return redirect(url_for('index'))

        # Carregar os tipos de notícias do arquivo JSON
        try:
            with open('news_types.json', 'r') as f:
                news_types = json.load(f)
        except FileNotFoundError:
            news_types = []  # Se o arquivo não existe, inicia uma lista vazia
        
        return render_template('edit_news.html', news=news_item, news_id=news_id, news_types=news_types)
    
    return redirect(url_for('index'))

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        title = request.form['title']  # Obtém o título da notícia
        news_type = request.form.get('news_type')  # Obtém o tipo selecionado
        description = request.form['description']   # Obtém a descrição da notícia
        
        # Cria um dicionário para a nova notícia
        new_news = {'title': title, 'description': description, 'type': news_type}
        
        # Adiciona a nova notícia à lista
        news_list.append(new_news)
        
        # Salva a lista atualizada no arquivo JSON
        save_news(news_list)
        
        return redirect(url_for('index'))  # Redireciona para a página inicial

    # Carregar os tipos de notícias do arquivo JSON
    try:
        with open('news_types.json', 'r') as f:
            news_types = json.load(f)
    except FileNotFoundError:
        news_types = []  # Se o arquivo não existe, inicia uma lista vazia
    
    return render_template('add_news.html', news_types=news_types)

@app.route('/remove_news/<int:news_id>', methods=['POST'])
def remove_news(news_id):
    # Remove a notícia da lista
    if 0 <= news_id < len(news_list):
        del news_list[news_id]
        # Salvar a lista atualizada no arquivo JSON
        save_news(news_list)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
