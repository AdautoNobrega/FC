from fcamara.models.models import Item, Categoria, Carrinho


class GerenciaItens:

    def __init__(self, dbsession):
        self.dbsession = dbsession

    def lista_itens(self):
        itens = self.dbsession.query(Item).all()
        return itens

    def lista_categorias(self):
        categorias = self.dbsession.query(Categoria).all()
        return categorias

    def lista_carrinho(self, id):
        carrinho = self.dbsession.query(Carrinho).filter(
            Carrinho.user_id == id
        ).all()
        return len(carrinho)
