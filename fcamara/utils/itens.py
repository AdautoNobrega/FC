from fcamara.models.models import Item, Compra


class GerenciaItens:

    def __init__(self, dbsession):
        self.dbsession = dbsession

    def lista_itens(self):
        result = []
        itens = self.dbsession.query(Item).all()
        for item in itens:
            result.append({'_id': str(item.id),
                           'nome': str(item.nome),
                           'imagem': item.imagem,
                           'descricao': item.descricao})
        return result


    def lista_carrinho(self, id):
        carrinho = self.dbsession.query(Compra).filter(
            Compra.user_id == id
        ).all()
        return len(carrinho)

    def adicionar_carrinho(self, id):
        item = self.dbsession.query(Item).filter(
            Item.id == id
        ).first()
        # carrinho = Compra(item,)
        return item
