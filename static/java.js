/**
 * Created by bezi on 2017.03.21..
 */

$(document).ready(function() {
    $( "#submit" ).click(function(e) {
        e.preventDefault();
        // ajax
        document.getElementById("myform").submit();
        return false;
    });
});





