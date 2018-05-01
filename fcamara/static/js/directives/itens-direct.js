angular.module('itensDirect', [])
    .directive('itensCard', function () {

        var ddo = {};

        ddo.restrict = "AE";
        ddo.transclude = true;


        ddo.scope = {
            id: '@',
            nome: '@',
            imagem: '@',
            descricao: '@'
        };

        ddo.templateUrl = 'static/js/directives/itens-card.html';

        return ddo;
    })
    .directive('carousel', function () {
        
        var ddo = {};

        ddo.restrict = "AE";
        ddo.transclude = true;


        ddo.scope = {
            id: '@',
            imagem: '@',
            nome: '@',
            descricao: '@'
        };

        ddo.templateUrl = 'static/js/directives/carousel.html';

        return ddo;
    })
