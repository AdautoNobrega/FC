angular.module('fc')
    .controller('LoginControl', function ($scope, $http, $routeParams) {

        $scope.user = {};
        $scope.mensagem = '';
        $scope.token = '';


        $scope.submeter = function () {

            if ($scope.formulariologin.$valid) {

                $http({
                    method: 'POST',
                    url: '/login',
                    data: { 'username': $scope.user.email, 'password': $scope.user.senha}
                }).then(function successCallback(response) {
                    $scope.mensagem = 'Usuário logado';
                    $scope.token = response.access_token
                }, function errorCallback(response) {
                    console.log(response)
                });
            }
            return $scope.token;
        };
    })
