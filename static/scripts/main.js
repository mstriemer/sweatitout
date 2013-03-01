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
                $email.val($('[name="email"]').val());
        } else if (payment_type == 'stripe') {
            var $card_name = $form.find('.card-name');
            if ($card_name.val() == '') {
                var name = $form.find('[name="first_name"]').val();
                if (name.length > 0)
                    name += ' ';
                name += $form.find('[name="last_name"]').val();
                $card_name.val(name);
            }
        }
    };

    $('input[name="payment_type"][checked]').each(show_payment_form);
    $('input[name="payment_type"]').on('click', show_payment_form);

    function stripeResponseHandler($form) {
        return function (status, response) {
            if (response.error) {
                // show the errors on the form
                $(".payment-errors").text(response.error.message);
                $(".submit-button").removeAttr("disabled");
            } else {
                // token contains id, last4, and card type
                var token = response.id;
                // insert the token into the form so it gets submitted to the server
                $form.append("<input type='hidden' name='stripe_card_token' value='" + token + "'/>");
                // and submit
                $form[0].submit();
            }
        };
    }

    window.StripeForm = function ($form) {
        this.$name = $form.find('.card-name');
        this.$number = $form.find('.card-number');
        this.$cvc = $form.find('.card-cvc');
        this.$exp_month = $form.find('.card-expiry-month');
        this.$exp_year = $form.find('.card-expiry-year');
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
            stripeForm = new StripeForm($form);
            var stripeData = stripeForm.formData();
            if (stripeForm.valid()) {
                $('.submit-button').attr("disabled", "disabled");

                Stripe.createToken(stripeData, stripeResponseHandler($form));
            }

            e.preventDefault();
        }
    });

    function show_element($el) {
        var scrollTo = $el.offset().top + $el.height() - window.innerHeight;
        if (scrollTo > window.pageYOffset) {
            $('body').animate({scrollTop: scrollTo}, 500);
        }
    }
});
