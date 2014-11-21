(function() {
    'use strict';

    angular.module('app', []).config(config);

    config.$inject = [ '$compileProvider' ];

    function config($compileProvider) {
        $compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|ftp|mailto|javascript):/);
    }

}());