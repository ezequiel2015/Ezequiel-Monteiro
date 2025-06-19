from flask import render_template, request, url_for, redirect
from models.database import db, Produto

def init_app(app):
    @app.route('/')
    def index():
        produtos = Produto.query.all()
        return render_template('index.html', produtos=produtos)

    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            produtos = Produto(request.form['nome'], request.form['valor'], request.form['descricao'])
            db.session.add(produtos)
            db.session.commit()
            return redirect(url_for('gerenciar'))
        return render_template('add.html')
    
    @app.route('/gerenciar', methods=['GET', 'POST'])
    def gerenciar():
        produtos = Produto.query.all()
        return render_template('gerenciar.html', produtos=produtos)

    @app.route('/edit/<int:id>', methods=['GET','POST'])
    def edit(id):
        produtos = Produto.query.get(id)
        if request.method == 'POST':
           
            produtos.nome = request.form['nome']
            produtos.valor = request.form['valor']
            produtos.descricao = request.form['descricao']
            db.session.commit()
            return redirect(url_for('gerenciar'))
        return render_template('edit.html', produtos = produtos)

    @app.route('/delete/<int:id>')
    def delete(id):
        produtos = Produto.query.get(id)
        # Deleta o dado, a partir da ID
        db.session.delete(produtos)
        db.session.commit()
        return redirect(url_for('gerenciar'))