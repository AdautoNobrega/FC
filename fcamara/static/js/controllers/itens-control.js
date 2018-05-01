angular.module('fc')
    .controller('ItensControl', function ($scope, $http) {

        $scope.itens = [];
        $scope.filtro = '';

        $http({
            method: 'GET',
            url: '/itens'
        }).then(function successCallback(response) {
            $scope.itens = response.data
        }, function errorCallback(response) {
            console.log(response)
        });

    });