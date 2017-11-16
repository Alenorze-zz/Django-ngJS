var app = angular.module('restang', []);
app.controler('restangControler', function($scope){
    $scope.restangList = [{restangText: 'Finish'}];
    $scope.restangAdd =- function() {
        $scope.restangList.push({restangText: $scope.todoInput});
        $scope.restangInput = '';
    };
});