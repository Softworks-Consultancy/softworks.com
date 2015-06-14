'use strict';

/* Controllers */

angular.module('softworks')

.controller('IndexController', ['$scope',function($scope){

}])

.controller('ContactController', ['$scope', '$http',function($scope, $http){

  $scope.contact = {};
  $scope.sent=true;

  $scope.contactus = function() {
    $scope.sent=false;
    if ($scope.contactform.$invalid) {return;}
    console.log($scope.contactform);
    $http.post("/api/v1/contact",
              $scope.contact)
      .then(function() { $scope.sent=true;});
  }

}])
