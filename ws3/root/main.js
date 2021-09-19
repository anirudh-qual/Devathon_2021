(function ($) {

    "use strict";

    var fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

})(jQuery);
var about = false;
var contacts = false;
function loadabout() {
    if (!about) {
        document.getElementsByClassName("text")[0].innerHTML =
            "Rhombus is a free tool for fast and secure access to scholarships." +
            "<br>Register-Apply-compete-win."
        about = true;
    }
    else {
        document.getElementsByClassName("text")[0].innerHTML = "";
        about = false;
    }
}
function loadcontacts() {
    if (!contacts) {
        document.getElementsByClassName("text")[0].innerHTML =
            "<a href=\"https://github.com/theWorkingPrototype\">Orange</a>" +
            "<br>" +
            "";
        contacts = true;
    }
    else {
        document.getElementsByClassName("text")[0].innerHTML = "";
        contacts = false;
    }
}