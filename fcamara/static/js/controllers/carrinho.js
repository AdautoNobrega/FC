angular.module('fc')

    .controller('Carrinho', function ($scope, $http) {

        $scope.carrinho = 0;

        $http({
            method: 'GET',
            url: '/carrinho'
        }).then(function successCallback(response) {
            $scope.carrinho = response.data
        }, function errorCallback(response) {
            console.log(response)
        });

    });