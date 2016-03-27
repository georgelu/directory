var App = angular.module('App', ['ui','angular.filter']);

App.controller('directoryCtrl', function($scope, $http) {
    $http.get('https://api.myjson.com/bins/3dnjr')
       .then(function(res){
          $scope.directory = res.data;
        });

    $scope.sortType     = 'timecode'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchName   = '';     // set the default search/filter term
    $scope.submit     = 'false'; // did a user submit feedback?

});
