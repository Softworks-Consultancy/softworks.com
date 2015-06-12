angular.module('cesar')

// .factory('LoginCache', ['CacheFactory',
//     function (CacheFactory) {
//   console.log('Cache initialised');
//   // Check to make sure the cache doesn't already exist
//     return CacheFactory('loginCache', {
//        storageMode: 'sessionStorage',
//        deleteOnExpire: 'aggressive',
//        capacity: 1,
//         });
// }])


.factory('CollegeListService', ['$resource',
  function($resource){
    return $resource('collegelist/collegejson.json', {}, {
      query: none
    });
  }]);