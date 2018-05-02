"""DataBase models for raspapreco mod1"""
import os

from sqlalchemy import (Boolean, Column, ForeignKey,
                        Integer, Numeric, String, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class MySession():
    """Para definir a sessão com o BD na aplicação."""

    def __init__(self, base, test=False):
        if test:
            path = ':memory:'
        else:
            path = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'fc.db')
            if os.name != 'nt':
                path = '/' + path
        self._engine = create_engine(
            'sqlite:///' + path, convert_unicode=True)
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


class Usuario(Base):
    """Tabela usuário."""
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String(20), unique=True)
    senha = Column(String(200), nullable=False)
    permissao = Column(Integer, default=1)
    compra = relationship('Compra', back_populates='usuarios')

    def __init__(self, email, senha, permissao):
        self.email = email
        self.senha = senha
        self.permissao = permissao

    @classmethod
    def get(cls, session, username, password):
        DBUser = session.query(Usuario).filter(
            Usuario.username == username,
            Usuario.password == password
        ).first()
        return DBUser


class Item(Base):
    """Tabela itens."""
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20))
    descricao = Column(String(50))
    imagem = Column(String())
    preco = Column(Numeric(asdecimal=False))
    categoria = Column(String(20))

    def __init__(self, nome, descricao, imagem, preco, categoria):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.preco = preco
        self.categoria = categoria


class Compra(Base):
    """Tabela compra."""
    __tablename__ = 'compra'
    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey('item.id'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship('Usuario', back_populates='compra')
    is_finalizado = Column(Boolean, default=False)

    def __init__(self, produto, usuario, finalizado):
        self.produto_id = produto.id
        self.usuario_id = usuario.id
        self.finalizado = finalizado


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
