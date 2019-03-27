$(document).ready(function () {
    $(document).ready(function(){
        var first = $("body").data("firstnav");
        var second = $("body").data("secondnav");                
        if(  first != 'undefined' ){
            first = "#" + first;             
            $(first) .addClass("active")
        }
        if(  second != 'undefined' ){
            second = "#" + second;             
            $(second) .addClass("active")
        }               
    });
});