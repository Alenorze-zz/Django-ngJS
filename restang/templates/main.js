var app = angular.module('restang', []);
app.controler('restangControler', function($scope){
    $scope.restangList = [{restangText: 'Finish', done: false}];
    $scope.restangAdd = function() {
        $scope.restangList.push({restangText: $scope.todoInput});
        $scope.restangInput = '';
    };
    $scope.remove = function() {
        var oldList = $scope.restangList;
        $scope.restangList = [];
        angular.forEach(oldList, function(x) {
           if (!x.done) $scope.restangList.push(x); 
        });
    };
});