/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})

window.onload = function() {
    location.hash = "#chart";
    window.scrollBy(0, 66); // additional scroll down by pixels.

    setTimeout(function() {
        const mainNav = document.getElementById('mainNav');
        mainNav.classList.add('is-visible');
    }, 500); // 0.5s delay
  }

$(document).ready(function() {
    $("#search-input").focus();
    $("#search-input").autocomplete({
        source: function( request, response ) {
            // filter the countries that starts with the input value
            response(data_search.filter(function(country) {
                return country.toLowerCase().startsWith(request.term.toLowerCase());
            }));
        },
        select: function( event, ui ) {
            // Fill the input field with the selected suggestion
            $("#search-input").val(ui.item.value);
            // Trigger the form submit when a suggestion is selected
            $("#search-form").submit();
        }
    });
});

function closeDropdown() {
    document.getElementById("navbarDropdown").click();
}

function titleCase(str) {
    return str.toLowerCase().replace(/(^|\s)[a-z]/g, function(match) {
    return match.toUpperCase();
    }).replace(/\b[a-z]/g, function(letter) {
    return letter.toUpperCase();
    });
}

function extractLast( term ) {
    return term.split( /,\s*/ ).pop();
}
