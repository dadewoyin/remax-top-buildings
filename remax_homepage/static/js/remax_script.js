$(window).load(function () { 
    $("#loader").fadeOut("slow");
    $('body').css('padding-top', parseInt($('#pageHeader').css("height")));
});

$(window).resize(function () { 
    $('body').css('padding-top', parseInt($('#pageHeader').css("height")));
});

$(document).ready(function(){
    //Apply coloring effect whether img or text is hovered over
    $(".imgNeighborhoodName").hover(function(){
        $(this).prev().css({
            "-webkit-filter":"grayscale(0%)",
            "filter":"grayscale(0%)"});
        }, function(){
        $(this).prev().css({
            "-webkit-filter":"grayscale(100%)",
            "filter":"grayscale(100%)"
        });
    });
});