angular.module('fc')
    .controller('ItensControl', function ($scope, $http) {

        $scope.itens = [];
        $scope.filtro = '';
        $scope.mensagem = ''
        $scope.isLogged = false;
        $scope.carrinho = 0;


        $http({
            method: 'GET',
            url: '/islogged'
        }).then(function successCallback(response) {
            $scope.isLogged = response.data;
        }, function errorCallback(response) {
            console.log(response);
        });

        $http({
            method: 'GET',
            url: '/carrinho'
        }).then(function successCallback(response) {
            $scope.carrinho = response.data;
        }, function errorCallback(response) {
            console.log(response);
        });

        $http({
            method: 'GET',
            url: '/itens'
        }).then(function successCallback(response) {
            $scope.itens = response.data;
        }, function errorCallback(response) {
            console.log(response);
        });

        $scope.adicionar_carrinho = function (id) {
            $http({
                method: 'POST',
                url: '/comprar?id=' + id
            }).then(function successCallback(response) {
                console.log(response.data);
                $scope.mensagem = response.data;
            }, function errorCallback(response) {
                console.log(response);
            });
        };

        $scope.logout = function () {
            $http({
                method: 'GET',
                url: '/logout'
            }).then(function successCallback(response) {
                console.log(response);
                $scope.isLogged = false;
            }, function errorCallback(response) {
                console.log(response);
            });
        };
    });