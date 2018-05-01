import os
from flask import Flask, jsonify, render_template, request
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_restful import Resource, Api
from .utils.itens import GerenciaItens
from .models.models import Base, Compra, Item, MySession, Usuario
from . import login

mysession = MySession(Base)
dbsession = mysession.session
engine = mysession.engine

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'algo-muito-secreto'
db = SQLAlchemy(app)
login.login_manager.init_app(app)
login.configure(app)
login.DBUser.dbsession = db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/itens')
def itens():
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_itens()
    return jsonify(result)


@app.route('/categorias')
def categorias():
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_itens()
    return jsonify(result)


@app.route('/comprar', methods=['GET', 'POST'])
def comprar():
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_itens()
    request.args.get('id')
    return jsonify(result)


@app.route('/carrinho', methods=['GET', 'POST'])
def carrinho():
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_itens()
    return jsonify(result)


@app.route('/islogged', methods=['GET'])
def is_logged():
    if current_user and current_user.is_authenticated:
        return jsonify(True)
    return jsonify(False)


Session(app)

if __name__ == '__main__':
    app.config['DEBUG']
    app.run()
