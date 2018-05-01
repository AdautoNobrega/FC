angular.module('fc')
  .controller('CarControl', function ($scope, $http) {
    $scope.myInterval = 5000;
    $scope.noWrapSlides = false;
    $scope.active = 0;
    var slides = $scope.slides = [];
    var currIndex = 0;


    $http({
      method: 'GET',
      url: '/itens'
    }).then(function successCallback(response) {
      $scope.slides = response.data
    }, function errorCallback(response) {
      console.log(response)
    });
  });