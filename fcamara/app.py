import os
from flask import Flask, jsonify, render_template, request
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from .utils.itens import GerenciaItens
from .models.models import Base, Compra, Item, MySession, Usuario
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
    return render_template('index.html')


@app.route('/itens')
def itens():
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_itens()
    return jsonify(result)


@app.route('/comprar', methods=['GET', 'POST'])
@login_required
def comprar():
    id = request.args.get('id')
    gerencia = GerenciaItens(dbsession)
    gerencia.adicionar_carrinho(id)
    return jsonify(id)


@app.route('/carrinho', methods=['GET', 'POST'])
@login_required
def carrinho():
    gerencia = GerenciaItens(dbsession)
    result = gerencia.lista_carrinho(1) # hard coded
    return jsonify(len(result))


@app.route('/islogged', methods=['GET'])
def is_logged():
    if current_user and current_user.is_authenticated:
        return jsonify(True)
    return jsonify(False)


if __name__ == '__main__':
    app.config['DEBUG']
    app.run()
