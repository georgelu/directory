var App = angular.module('App', ['ui','angular.filter','ui.bootstrap']);

App.controller('directoryCtrl', function($scope, $http, $uibModal, $log) {
    $http.get('https://api.myjson.com/bins/3dnjr')
       .then(function(res){
          $scope.directory = res.data;
        });

    //Search + Sort Filters
    $scope.sortType     = 'timecode'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    $scope.searchName   = '';     // set the default search/filter term
    $scope.submit     = 'false'; // did a user submit feedback?

    // MODAL WINDOW
    $scope.open = function () {

        var modalInstance = $uibModal.open({
            templateUrl: 'detailModal.html',
            controller: "ModalInstanceCtrl",
            resolve: {
                items: function()
                {
                    return $scope.directory;
                }
            }
             });
    };
});

App.controller('ModalInstanceCtrl', function ($scope, $uibModalInstance, items) {
  $scope.items = items;

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});
