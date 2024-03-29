/**
 * Created by Sandeep on 01/06/14.
 */
 
angular.module('movieApp.services',[]).factory('Movie',function($resource){
    return $resource('/api/entries/:id',{id:'@_id'},{
        update: {
            method: 'PUT'
        }
    });
}).service('popupService',function($window){
    this.showPopup=function(message){
        return $window.confirm(message);
    }
});