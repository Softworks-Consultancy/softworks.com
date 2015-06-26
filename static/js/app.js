'use strict';

// Declare app level module which depends on views, and components
angular.module('softworks', [
  'ngRoute',
  'ui.bootstrap',
  'ngMaps',
])
.config(function($interpolateProvider) {
   $interpolateProvider.startSymbol('[[');
   $interpolateProvider.endSymbol(']]');
})
.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}])
.config(['$routeProvider', function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'partials/intro',
        controller: 'IndexController'
    }).when('/services', {
        templateUrl: 'partials/services',
        controller: 'IndexController'
    }).when('/clients', {
        templateUrl: 'partials/clients',
        controller: 'IndexController'
    }).when('/contact', {
        templateUrl: 'partials/contact',
        controller: 'ContactController'
    })
    .otherwise({redirectTo: '/'});
}])
