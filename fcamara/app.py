"""
Módulo FC
=========
"""
import os
from flask import Flask, jsonify, render_template, request
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from .utils.itens import GerenciaItens
from .models.models import Base, MySession
from . import login

mysession = MySession(Base)
dbsession = mysession.session
engine = mysession.engine

path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'fc.db')

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'algo-muito-secreto'
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login.login_manager.init_app(app)
login.configure(app)
login.DBUser.dbsession = db


@app.route('/')
def index():
    """Renderiza o template."""
    return render_template('index.html')


@app.route('/itens')
def itens():
    """Função que retorna os itens."""
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_itens()
    return jsonify(result)


@app.route('/comprar', methods=['GET', 'POST'])
@login_required
def comprar():
    """Função que adiciona itens ao carrinho."""
    itemid = request.args.get('itemid')
    gerencia = GerenciaItens(dbsession)
    response = gerencia.adicionar_carrinho(itemid)
    return jsonify(response)


@app.route('/carrinho', methods=['GET', 'POST'])
@login_required
def carrinho():
    """Função que retorna a quantidade de itens ao carrinho."""
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_carrinho(1)  # hard coded
    return jsonify(result)


@app.route('/islogged', methods=['GET'])
def is_logged():
    """Verifica se o usuário está logado."""
    if current_user and current_user.is_authenticated:
        return jsonify(True)
    return jsonify(False)


if __name__ == '__main__':
    app.config['DEBUG']
    app.run()
