jQuery(function ($) {
    $('.signup').on('click', function (e) {
        var $form = $('.course-signup-form');
        $form.show();
        $('input', $form)[0].focus();
        $(this).hide();
        show_element($form);
        e.preventDefault();
    });

    $('.no-signup').on('click', function (e) {
        $('.course-signup-form').hide();
        $('.signup').show();
        e.preventDefault();
    });

    $('input[name="payment_type"][checked]').each(show_payment_form);
    $('input[name="payment_type"]').on('click', show_payment_form);

    function show_payment_form() {
        var payment_type = $(this).val();
        var class_name = 'payment-info-' + payment_type;
        var $payment_type = $('.' + class_name);
        $payment_type.show();
        $('.payment-info').each(function () {
            if (!$(this).hasClass(class_name))
                $(this).hide();
        });
        show_element($payment_type.parents('form'));
        if (payment_type == 'paypal') {
            var $email = $('[name="paypal_email"]');
            if ($email.val() == '')
                $email.val($('[name="email"]').val());
        }
    };

    function show_element($el) {
        var scrollTo = $el.offset().top + $el.height() - window.innerHeight;
        if (scrollTo > window.pageYOffset) {
            $('body').animate({scrollTop: scrollTo}, 500);
        }
    }
});
