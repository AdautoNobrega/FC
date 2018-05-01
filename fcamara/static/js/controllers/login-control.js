angular.module('fc')
    .controller('LoginControl', function ($scope, $http, $routeParams) {

        $scope.user = {};
        $scope.mensagem = '';
        $scope.token = '';


        $scope.submeter = function () {

            if ($scope.formulariologin.$valid) {

                $http({
                    method: 'POST',
                    url: '/auth',
                    data: { 'username': $scope.user.nome, 'password': $scope.user.senha, }
                }).then(function successCallback(response) {
                    $scope.mensagem = 'Foi';
                    $scope.token = response.access_token
                }, function errorCallback(response) {
                    console.log(response)
                });
            }
            return $scope.token;
        };
    })
