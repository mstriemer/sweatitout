jQuery(function ($) {
    $('.signup').on('click', function (e) {
        var $form = $('.course-signup-form');
        $form.show();
        $('input', $form)[0].focus();
        $('body').animate({scrollTop: $form.offset().top}, 1000);
        $(this).hide();
        e.preventDefault();
    });

    $('.no-signup').on('click', function (e) {
        $('.course-signup-form').hide();
        $('.signup').show();
        e.preventDefault();
    });

    var show_payment_form = function () {
        var payment_type = $(this).val();
        var class_name = 'payment-info-' + payment_type;
        var $payment_type = $('.' + class_name);
        $payment_type.show();
        $('.payment-info').each(function () {
            if (!$(this).hasClass(class_name))
                $(this).hide();
        });
        $('body').animate({scrollTop: $payment_type.offset().top}, 1000);
        if (payment_type == 'paypal') {
            var $email = $('[name="paypal_email"]');
            if ($email.val() == '')
                $email.val($('[name="email"]').val());
        }
    };

    $('input[name="payment_type"][checked]').each(show_payment_form);
    $('input[name="payment_type"]').on('click', show_payment_form);
});
