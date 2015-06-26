'use strict';

/* Controllers */

angular.module('softworks')

.controller('IndexController', ['$scope',function($scope){

}])

.controller('ContactController', ['$scope', '$http',function($scope, $http){

  $scope.map = {
    center: [3.1636780,101.6556520],
    options: function() {
      return {
        streetViewControl: false,
        scrollwheel: false,
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.HYBRID,
      }
    }
  };

  $scope.infowindow = {
    position: [3.1644707,101.6556305]
  }

  $scope.marker = {
    position: [3.1636780,101.6556520],
    events: {
        click: function(e) {
          $scope.infowindow.position = e.latLng;
          $scope.$apply()
      }
    }
  }

  $scope.contact = {};
  $scope.sent=false;


  $scope.contactus = function() {
    $scope.sent=false;
    if ($scope.contactform.$invalid) {return;}
    console.log($scope.contact);
    $http.post("/api/v1/contact/",
              $scope.contact)
      .then(function() { $scope.sent=true;});
  }

}])
