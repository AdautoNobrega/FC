angular.module('fc', ['itensDirect', 'ngAnimate', 'ngRoute', 'ngResource'])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });;

    $routeProvider.when('/produtos', {
      templateUrl: '/static/partials/produtos.html',
      controller: 'ItensControl',
    });

    $routeProvider.when('/login', {
      templateUrl: '/static/partials/login.html',
      controller: 'LoginControl'
    });


    $routeProvider.otherwise({ redirectTo: '/produtos' });

  });