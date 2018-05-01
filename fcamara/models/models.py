"""DataBase models for raspapreco mod1"""
import os

from sqlalchemy import (Boolean, Column, ForeignKey, Integer, LargeBinary,
                        Numeric, PickleType, String, Table, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class Permissao:
    COMPRAR = 1
    CADASTRAR = 2


class MySession():
    def __init__(self, base, test=False):
        path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'fc.db')
        if os.name != 'nt':
            path = '/' + path
        self._engine = create_engine(
            'postgresql://' + path, convert_unicode=True)
        Session = sessionmaker(bind=self._engine)
        self._session = scoped_session(Session)
        base.metadata.bind = self._engine

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    _password = Column(String(200))

    def __init__(self, username, password, permissao):
        self.username = username
        self._password = self.encript(password)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    descricao = Column(String(50))
    imagem = Column(String())
    preco = Column(Numeric(asdecimal=False))

    def __init__(self, nome, descricao, imagem, preco):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.preco = preco


class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    nome = Column(Integer, unique=True)


class Carrinho(Base):
    __tablename__ = 'carrinho'
    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey('item.id'))
    usuario_id = Column(Integer, ForeignKey('user.id'))
    finalisado = Column(Boolean)


class CarrinhoProduto(Base):
    __tablename__ = 'carrinhoitem'
    id = Column(Integer, primary_key=True)
    


if __name__ == '__main__':
    import alembic.config
    alembicArgs = [
        'revision',
        '--autogenerate', '-m "from code"',
    ]
    alembic.config.main(argv=alembicArgs)
    alembicArgs = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembicArgs)
