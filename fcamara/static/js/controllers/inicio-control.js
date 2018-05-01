angular.module('fc')
    .controller('InicioControl', function ($scope, $http, $routeParams) {
        $scope.isLogged = false;
        $scope.carrinho = 0;


        $http({
            method: 'GET',
            url: '/islogged'
        }).then(function successCallback(response) {
            $scope.isLogged = response.data
        }, function errorCallback(response) {
            console.log(response)
        });


        $http({
            method: 'GET',
            url: '/carrinho'
        }).then(function successCallback(response) {
            $scope.carrinho = response.data
        }, function errorCallback(response) {
            console.log(response)
        });
    });