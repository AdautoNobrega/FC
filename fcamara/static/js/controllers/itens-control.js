angular.module('fc')
    .controller('ItensControl', function ($scope, $http) {

        $scope.itens = [];
        $scope.filtro = '';

        $scope.carrinho = function (id) {
            $http({
                method: 'POST',
                url: '/comprar?id=' + id
            }).then(function successCallback(response) {
                console.log(response.data)
            }, function errorCallback(response) {
                console.log(response)
            });
        };

        $http({
            method: 'GET',
            url: '/itens'
        }).then(function successCallback(response) {
            $scope.itens = response.data
        }, function errorCallback(response) {
            console.log(response)
        });

    });