jQuery(function ($) {
    $('.assessments_field').each(function () {
        assessmentsInfo($(this));
    });

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

    function assessmentsInfo($el) {
        var link = $('<a href="#tell-me-more">Tell me more</a>');
        var explainationText = "Want a little extra help attaining your fitness goals? Add our new accountability package onto any group fitness class. This package gives you 3 assessments at the beginning, mid point and end of the session which include weight, measurements and photos to track your progress. Simply select the accountability add on when you complete your registration, and get ready to see results! $20.00 with any group fitness registration.";
        var explainationInner = $('<div class="controls tell-me-more"></div>')
        var explaination = $('<div style="display: none;" class="control-group"></div>');
        explainationInner.text(explainationText);
        explaination.html(explainationInner);
        link.on('click', function () { explaination.toggle(); });
        $el.find('label').append(link);
        $el.after(explaination);
    }

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
