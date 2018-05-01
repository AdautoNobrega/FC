angular.module('listaItens', ['ngResource'])
    .factory('listaItem', function ($resource) {
        return $resource('/itens/:itemId', null, {
            'update': {
                method: 'PUT'
            }
        });
    })
    .factory("cadastroItens", function (listaItens, $q) {
        var service = {};
        service.cadastrar = function (item) {
            return $q(function (resolve, reject) {

                listaItens.save(item, function () {
                    resolve({
                        mensagem: 'Item ' + item.nome + ' incluído com sucesso',
                        inclusao: true
                    });
                }, function (erro) {
                    console.log(erro);
                    reject({
                        mensagem: 'Não foi possível incluir o item ' + item.nome
                    });
                });
            });
        };
        return service;
    });
