from fcamara.models.models import Item, Compra, Usuario


class GerenciaItens:
    """Classe responsável pela comunicação entre a View e o Banco de Dados."""

    def __init__(self, dbsession):
        self.dbsession = dbsession

    def lista_itens(self):
        """Realiza uma busca no Banco de Dados e traz uma lista de objetos.

        Esta lista é passada para um dicionário.
        """
        result = []
        itens = self.dbsession.query(Item).all()
        for item in itens:
            result.append({'id': str(item.id),
                           'nome': str(item.nome),
                           'imagem': item.imagem,
                           'descricao': item.descricao})
        return result

    def lista_carrinho(self, id):
        """Realiza uma busca no Banco de Dados e traz uma lista de objetos.

        Este método está *hard coded*

        Args:
            id: id do usuário.
        """
        carrinho = self.dbsession.query(Compra).filter(
            Compra.usuario_id == id
        ).all()
        return len(carrinho)

    def adicionar_carrinho(self, itemid, user='fcamara'):
        """Adiciona um item ao carrinho.

        Este método está *hard coded*

        Args:
            id: id do usuário
            user: nome do usuário
        """
        item = self.dbsession.query(Item).filter(
            Item.id == itemid
        ).first()
        usuario = self.dbsession.query(Usuario).filter(
            Usuario.email == user
        ).first()
        if item and usuario:
            carrinho = Compra(item.id, usuario.id, False)
            self.dbsession.add(carrinho)
            self.dbsession.commit()
            return 'Item adicionado ao carrinho!'
        return 'Não foi possível adicionar'
