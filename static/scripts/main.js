jQuery(function ($) {
    $('.signup').on('click', function (e) {
        var $course = $(e.currentTarget).parents('.course');
        var $form = $course.find('.course-signup-form');
        $form.show();
        $form.find('input')[0].focus();
        $(this).hide();
        show_element($form);
        e.preventDefault();
    });

    $('.no-signup').on('click', function (e) {
        var $course = $(e.currentTarget).parents('.course');
        $course.find('.course-signup-form').hide();
        $course.find('.signup').show();
        e.preventDefault();
    });

    $('input[name="payment_type"][checked]').each(show_payment_form);
    $('input[name="payment_type"]').on('click', show_payment_form);

    // `show_payment_form` is not a very descriptive name.
    function show_payment_form() {
        var $payment_el = $(this); // Using `this` is gross.
        var $form = $payment_el.parents('form');
        var payment_type = $payment_el.val();
        var class_name = 'payment-info-' + payment_type;
        $form.find('.payment-info').each(function () {
            var $el = $(this);
            if ($el.hasClass(class_name))
                $el.show();
            else
                $el.hide();
        });
        show_element($form);
        if (payment_type == 'paypal') {
            var $email = $form.find('[name="paypal_email"]');
            if ($email.val() == '')
                $email.val($form.find('[name="email"]').val());
        }
    };

    function show_element($el) {
        var scrollTo = $el.offset().top + $el.height() - window.innerHeight;
        if (scrollTo > window.pageYOffset) {
            $('body').animate({scrollTop: scrollTo}, 500);
        }
    }
});
