
from urllib.parse import urljoin, urlparse

from flask import abort, redirect, render_template, request, url_for, jsonify
from flask_login import (LoginManager, UserMixin, login_required, login_user,
                         logout_user)
from werkzeug.security import check_password_hash, generate_password_hash

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'


def configure(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            registered_user = authenticate(username, password)
            if registered_user is not None:
                print('Logged in..')
                print(login_user(registered_user))
                # print('Current user ', current_user)
                next_url = request.args.get('next')
                if not is_safe_url(next_url):
                    return abort(400)
                return jsonify('Not Secure')
            else:
                return abort(401)
        else:
            return jsonify('Logged')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        next = request.args.get('next')
        if not is_safe_url(next):
            next = None
        return jsonify('Logged out')


@login_manager.unauthorized_handler
def unauthorized():
    message = 'Não autorizado! ' + \
        'Efetue login novamente com usuário e senha válidos.'
    return jsonify(message)


class DBUser():

    dbsession = None

    def __init__(self, id, password=None):
        self.id = id
        self.name = str(id)
        self._password = password

    @classmethod
    def add(cls, username, password):
        if not cls.dbsession:
            raise Exception('Sem conexão com o Banco de Dados!')
        cursor = cls.dbsession.users.update(
            {'username': username},
            {'username': username,
             'password': password},
            upsert=True)
        print('cursor', cursor)
        return DBUser.get(username, password)

    @classmethod
    def get(cls, username, password=None):
        if cls.dbsession:
            return DBUser(username)
        else:
            if username:
                if not password:
                    return DBUser(username, password)
                if username == password:
                    return DBUser(username, password)
        return None


class Usuario(UserMixin):
    """Mixin padrão do flask-login.

    Está utilizando DBUser como base de autenticação.
    Para utilizar outra base de dados, criar outra classe com
    comportamento similar a DBUSer.

    """

    user_database = DBUser

    def __init__(self, id):
        """Instancia Usuario."""
        self.id = id
        self.name = str(id)

    @classmethod
    def get(cls, username, password=None):
        """Consulta DBUser."""
        dbuser = cls.user_database.get(username, password)
        if dbuser:
            return Usuario(dbuser.name)
        return None


def authenticate(username, password):
    """Método padrão do flask-login. Repassa responsabilidade a Usuario."""
    user_entry = Usuario.get(username, password)
    # print('authenticate user entry ', user_entry)
    return user_entry


@login_manager.user_loader
def load_user(userid):
    """Método padrão do flask-login. Repassa responsabilidade a Usuario."""
    user_entry = Usuario.get(userid)
    return user_entry


def is_safe_url(target):
    """Testa ocorrência de ataque de redirecionamento(URL Redirect/Pishing)."""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc
