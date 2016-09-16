function init () {
    $('input').keypress( function(){
        $('.has-error').hide();
    });
}


jQuery(document).ready(function ($) {
    init();
});