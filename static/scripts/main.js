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
        } else if (payment_type == 'stripe') {
            var $card_name = $('#card-name-input');
            if ($card_name.val() == '') {
                var name = $('[name="first_name"]').val();
                if (name.length > 0)
                    name += ' ';
                name += $('[name="last_name"]').val();
                $card_name.val(name);
            }
        }
    };

    $('input[name="payment_type"][checked]').each(show_payment_form);
    $('input[name="payment_type"]').on('click', show_payment_form);

    function stripeResponseHandler(status, response) {
        if (response.error) {
            // show the errors on the form
            $(".payment-errors").text(response.error.message);
            $(".submit-button").removeAttr("disabled");
        } else {
            var $form = $(".stripe-form");
            // token contains id, last4, and card type
            var token = response.id;
            // insert the token into the form so it gets submitted to the server
            $form.append("<input type='hidden' name='stripe_card_token' value='" + token + "'/>");
            // and submit
            $form[0].submit();
        }
    }

    window.StripeForm = function () {
        this.$name = $('.card-name');
        this.$number = $('.card-number');
        this.$cvc = $('.card-cvc');
        this.$exp_month = $('.card-expiry-month');
        this.$exp_year = $('.card-expiry-year');
        var addError = function ($el, error) {
            $el.siblings('.help-inline').text(error);
            $el.parents('.control-group').addClass('error');
        };
        var clearError = function ($el) {
            $el.siblings('.help-inline').text('required');
            $el.parents('.control-group').removeClass('error');
        };
        this.valid = function () {
            var _this = this;
            var validate = function ($el, message, validator) {
                var valid = validator.call(_this, $el);
                if (valid) clearError($el);
                else addError($el, message);
                return valid;
            };
            var validations = [
                validate(this.$name, 'required', function ($el) {
                    return $el.val().length > 0;
                }),
                validate(this.$number, 'not a valid card number', function ($el) {
                    return Stripe.validateCardNumber($el.val());
                }),
                validate(this.$cvc, 'not a valid CVC', function ($el) {
                    return Stripe.validateCVC($el.val());
                }),
                validate(this.$exp_year, 'not a valid expiry date', function ($el) {
                    return Stripe.validateExpiry(this.$exp_month.val(), this.$exp_year.val());
                })
            ];
            var valid = true;
            for (var i = 0; i < validations.length; i++) {
                valid = valid && validations[i];
            }
            return valid;
        };
    };
    StripeForm.prototype = {
        formData: function () {
            return {
                name: this.$name.val(),
                number: this.$number.val(),
                cvc: this.$cvc.val(),
                exp_month: this.$exp_month.val(),
                exp_year: this.$exp_year.val()
            };
        },
    };

    $(".stripe-form").on('submit', function (e) {
        var $form = $(this);
        var $stripe_payment = $('input[name="payment_type"][value="stripe"]', $form);
        if ($stripe_payment[0].checked) {
            stripeForm = new StripeForm();
            var stripeData = stripeForm.formData();
            if (stripeForm.valid()) {
                $('.submit-button').attr("disabled", "disabled");

                Stripe.createToken(stripeData, stripeResponseHandler);
            }

            e.preventDefault();
        }
    });
});
