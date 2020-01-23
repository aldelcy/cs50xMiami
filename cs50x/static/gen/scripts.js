'use strict';

new TypeIt('#hero', {
    speed: 40,
    waitUntilVisible: true,
    cursor: false
}).go();

new TypeIt('#welcome_cohort_title', {
    speed: 70,
    waitUntilVisible: true
}).go();

new TypeIt('#masterclass_title', {
    speed: 95,
    waitUntilVisible: true
}).go();







// ACTIVITIES

// SPY YPS SPY 

var passwords = [
    "01100010 01100001 01111010 01101001 01101110 01100111 01100001",
    "01010000 01100001 01110011 01110011 01010111 01101111 01110010 01100100",
    "01101101 01100001 01010010 01101001 01101111",
    "01010000 01101001 01111010 01111010 01000001",
    "01010010 01100101 01100100 01010010 01110101 01101101",
    "01010001 01010111 01000101 01010010 01010100 01011001"
]

$('div#password').text( passwords[ Math.floor(Math.random() * passwords.length) ] );

$('.submit_password').click(function(){
    $.ajax({
        url:'/spy_submission',
        type:'POST',
        data: { level: 1, code: $('input#thePassword').val() },
        success: function (data){
            if( data[0] ){
                $('.phase_1').hide();
                $('.phase_2').fadeIn(3000);
                $('.phase_2').find('textarea').attr("data-code", data[1]);
                $('.the_secret_image').html( `<img src="/static/assets/activities/spy/Binary_${data[1]}.png">` )
            }else{
                $('#error_message').text( "WHOOOPS! Wrong password !!" + data[1]  );
                $('#error_message').fadeIn( 500  );
                setTimeout( function(){
                    $('#error_message').fadeOut( 500  );
                }, 4000);
                setTimeout( function(){
                    $('#error_message').empty( );
                }, 4500);
            };
        }
    })
});

$('.submit_thecode').click(function(){
    var code = $('textarea#theCode');
    $.ajax({
        url:'/spy_submission',
        type:'POST',
        data: { level: 2, code: code.data('code')+"+"+code.val() },
        success: function (data){
            if( data[0] ){
                $('.phase_2').hide();
                $('.phase_3').fadeIn(3000);
                $('.phase_3').find('.message').html(`<h2 class='bold'>${data[1]}</h2>`);
            }else{
                $('#error_message').text( "OUUUUFFF, that's not the right Secret Code !! " + data[1]  );
                $('#error_message').fadeIn( 500  );
                setTimeout( function(){
                    $('#error_message').fadeOut( 500  );
                }, 4000);
                setTimeout( function(){
                    $('#error_message').empty( );
                }, 4500);
            };
        }
    })
});