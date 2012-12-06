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
            console.log(this, class_name, $(this).hasClass(class_name));
            if (!$(this).hasClass(class_name)) {
                $(this).hide();
            }
        });
        $('body').animate({scrollTop: $payment_type.offset().top}, 1000);
        if (payment_type == 'paypal') {
            var $email = $('[name="paypal[email]"]');
            if ($email.val() == '')
                $email.val($('[name="email"]').val());
        } else if (payment_type == 'stripe') {
            var $card_name = $('#card-name-input');
            if ($card_name.val() == '')
                $card_name.val(
                        $('[name="first_name"]').val() +
                        ' ' +
                        $('[name="last_name"]').val());
        }
    };

    $('input[name="payment_type"][checked]').each(show_payment_form);
    $('input[name="payment_type"]').on('click', show_payment_form);

    function stripeResponseHandler(status, response) {
        console.log(status, response);
        if (response.error) {
            // show the errors on the form
            $(".payment-errors").text(response.error.message);
            $(".submit-button").removeAttr("disabled");
        } else {
            var form$ = $(".stripe-form");
            // token contains id, last4, and card type
            var token = response['id'];
            // insert the token into the form so it gets submitted to the server
            form$.append("<input type='hidden' name='stripeToken' value='" + token + "'/>");
            // and submit
            form$.get(0).submit();
        }
    }

    // $(".stripe-form").on('submit', function (event) {
    //     // disable the submit button to prevent repeated clicks
    //     $('.submit-button').attr("disabled", "disabled");

    //     Stripe.createToken({
    //         number: $('.card-number').val(),
    //         cvc: $('.card-cvc').val(),
    //         exp_month: $('.card-expiry-month').val(),
    //         exp_year: $('.card-expiry-year').val()
    //     }, stripeResponseHandler);

    //     // prevent the form from submitting with the default action
    //     return false;
    // });
});
