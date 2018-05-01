from fcamara.models.models import Item, Compra


class GerenciaItens:

    def __init__(self, dbsession):
        self.dbsession = dbsession

    def lista_itens(self):
        result = []
        itens = self.dbsession.query(Item).all()
        for item in itens:  
            result.append({'_id':str(item.id),
                        'nome': str(item.nome),
                        'imagem': item.imagem,
                        'descricao': item.descricao})
        return result

    """def lista_categorias(self):
        categorias = self.dbsession.query(Categoria).all()
        return categorias"""

    def lista_carrinho(self, id):
        carrinho = self.dbsession.query(Carrinho).filter(
            Carrinho.user_id == id
        ).all()
        return len(carrinho)
