(function ($) {
    "use strict";



    // Dropdown on mouse hover
    // $(document).ready(function () {
    //     function toggleNavbarMethod() {
    //         if ($(window).width() > 992) {
    //             $('.navbar .dropdown').on('mouseover', function () {
    //                 $('.dropdown-toggle', this).trigger('click');
    //             }).on('mouseout', function () {
    //                 $('.dropdown-toggle', this).trigger('click').blur();
    //             });
    //         } else {
    //             $('.navbar .dropdown').off('mouseover').off('mouseout');
    //         }
    //     }
    //     toggleNavbarMethod();
    //     $(window).resize(toggleNavbarMethod);
    // });

    // $(document).ready(function () {
    //     function toggleDropdown() {
    //         if ($(window).width() > 992) {
    //             $('.nav-item.dropdown').on('mouseenter', function () {
    //                 $(this).find('.dropdown-menu').addClass('show');
    //             }).on('mouseleave', function () {
    //                 $(this).find('.dropdown-menu').removeClass('show');
    //             });
    //         } else {
    //             $('.nav-item.dropdown').off('mouseenter').off('mouseleave');
    //         }
    //     }

    //     toggleDropdown(); // Initial setup
    //     $(window).resize(toggleDropdown); // Update on window resize
    // });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: true,
        loop: true,
        items: 1
    });

})(jQuery);

