angular.module('fc', ['itensDirect', 'ngAnimate', 'ngRoute', 'ngResource', 'ui.carousel'])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });;

    $routeProvider.when('/', {
      templateUrl: '/static/partials/home.html',
      controller: 'CarControl'
    });

    $routeProvider.when('/produtos', {
      templateUrl: '/static/partials/produtos.html',
      controller: 'ItensControl'
    });
    
    $routeProvider.when('/carrinho', {
      templateUrl: '/static/partials/compra.html',
      controller: 'Carrinho'
    });

    $routeProvider.when('/cadastro/itens', {
      templateUrl: '/static/partials/cadastroitens.html',
      controller: 'ItensControl'
    });

    $routeProvider.when('/cadastro/usuario', {
      templateUrl: '/static/partials/cadastrousuario.html'
    });

    $routeProvider.when('/login', {
      templateUrl: '/static/partials/login.html',
      controller: 'LoginControl'
    });


    //$routeProvider.otherwise({ redirectTo: '/' });

  });