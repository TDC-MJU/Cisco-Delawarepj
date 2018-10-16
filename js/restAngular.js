'use strict';

var dmeApp = angular.module('pogoApp', []);

dmeApp.controller('pogoCtrl', function ($scope, $http) {
    $http.get('/py/return.py').success(function(data, status, headers, config) {
        console.log('success');
        //receiving json back
        $scope.entries= data.entries;
        //printing out the returned json
        console.log(data);
    }).error(function(data, status, headers, config) {
        console.log('error');
        console.log(arguments);
    });

    if (navigator.geolocation) navigator.geolocation.getCurrentPosition(onPositionUpdate);
 
    function onPositionUpdate(position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        var url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + lng + "&sensor=true";
        $http.get(url)
            .then(function(result) {
                var address = result.data.results[2].formatted_address;
                $scope.address = address;
                console.log(address)
            });
    }

    $scope.initMap = function(pokemon_id, pokemon_location) {
        document.getElementById('map_'+pokemon_id).innerHTML = ''
        // var map = new google.maps.Map(document.getElementById('map_'+pokemon_id), {
        //     center: pokemon_location,
        //     zoom: 18
        //   });
    }
});

