import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import RegistrationForm, Base, Course

def make_course(**kwargs):
    return Course(**kwargs)

def make_form(first_name="Bob", last_name="Smith",
        email="bob.smith@gmail.com", phone="204-555-1234",
        payment_type='in_person', course_slug="the-course",
        attendance='both', course=None, **kwargs):
    if course is None:
        course = make_course(half_cost=60)
    return RegistrationForm(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            payment_type=payment_type,
            course_slug=course_slug,
            attendance=attendance,
            instance=course,
            **kwargs)


class TestRegistrationFormValid(unittest.TestCase):
    def test_valid(self):
        form = make_form()
        self.assertTrue(form.valid())

    def test_first_name_required(self):
        form = make_form(first_name='')
        self.assertFalse(form.valid())

    def test_last_name_required(self):
        form = make_form(last_name='')
        self.assertFalse(form.valid())

    def test_email_required(self):
        form = make_form(email='')
        self.assertFalse(form.valid())

    def test_phone_required(self):
        form = make_form(phone='')
        self.assertFalse(form.valid())

    def test_invalid_email_no_name(self):
        form = make_form(email='smith.com')
        self.assertFalse(form.valid())

    def test_invalid_email_no_tld(self):
        form = make_form(email='bob@smith')
        self.assertFalse(form.valid())

    def test_invalid_email_partial_tld(self):
        form = make_form(email='bob@smith.')
        self.assertFalse(form.valid())

    def test_invalid_email_partial_name(self):
        form = make_form(email='@smith.com')
        self.assertFalse(form.valid())

    def test_invalid_email_no_domain(self):
        form = make_form(email='bob@.smith')
        self.assertFalse(form.valid())

    def test_invalid_email_multiple_ats(self):
        form = make_form(email='bob@smith@gmail.com')
        self.assertFalse(form.valid())

    def test_invalid_phone_number_too_short(self):
        form = make_form(phone='5551234')
        self.assertFalse(form.valid())

    def test_invalid_phone_number_other_characters(self):
        form = make_form(phone='--\\//..  .204----11..  ')
        self.assertFalse(form.valid())

    def test_invalid_no_attendance(self):
        form = make_form(attendance=None)
        self.assertFalse(form.valid())

    def test_valid_no_attendance_when_not_required(self):
        course = make_course(half_cost=None)
        form = make_form(attendance=None, course=course)
        self.assertTrue(form.valid())

    def test_invalid_options_are_not_allowed(self):
        form = make_form(payment_type='none')
        self.assertFalse(form.valid())

    def test_paypal_email_for_paypal_required(self):
        form = make_form(payment_type='paypal', paypal_email='')
        self.assertFalse(form.valid())

    def test_paypal_email_for_paypal_is_email(self):
        form = make_form(payment_type='paypal', paypal_email='mark@striemer')
        self.assertFalse(form.valid())

    def test_paypal_email_for_paypal_is_valid(self):
        form = make_form(payment_type='paypal', paypal_email='me@example.org')
        self.assertTrue(form.valid())

    def test_stripe_card_token_for_stripe_required(self):
        form = make_form(payment_type='stripe', stripe_card_token='')
        self.assertFalse(form.valid())

    def test_stripe_card_token_for_stripe_is_valid(self):
        form = make_form(payment_type='stripe', stripe_card_token='foobar')
        self.assertTrue(form.valid())


class TestRegistrationFormSave(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def assertValidRegistration(self, **kwargs):
        form = make_form(**kwargs)
        registration = form.build()
        self.assertIs(registration.id, None)
        self.session.add(registration)
        self.session.commit()
        self.assertTrue(registration.id > 0)
        return registration

    def test_build_returns_a_saveable_registration_in_person(self):
        reg = self.assertValidRegistration(payment_type='in_person')
        self.assertEqual(reg.payment_type, 'in_person')

    def test_build_returns_a_saveable_registration_stripe(self):
        reg = self.assertValidRegistration(payment_type='stripe',
                stripe_card_token='foobar')
        self.assertEqual(reg.payment_type, 'stripe')
        self.assertEqual(reg.stripe_card_token, 'foobar')

    def test_build_returns_a_saveable_registration_paypal(self):
        reg = self.assertValidRegistration(payment_type='paypal',
                paypal_email='foo@bar.com')
        self.assertEqual(reg.payment_type, 'paypal')
        self.assertEqual(reg.paypal_email, 'foo@bar.com')

    def test_cost_is_pulled_from_course_no_attendance(self):
        course = make_course(cost=200)
        reg = self.assertValidRegistration(course=course)
        self.assertEqual(reg.cost, 200)

    def test_cost_is_pulled_from_course(self):
        course = make_course(cost=110, half_cost=50)
        reg = self.assertValidRegistration(attendance='both', course=course)
        self.assertEqual(reg.cost, 110)

    def test_half_cost_is_pulled_from_course(self):
        course = make_course(cost=110, half_cost=50)
        reg = self.assertValidRegistration(attendance='tuesdays', course=course)
        self.assertEqual(reg.cost, 50)

    def test_build_raises_an_exception_when_invalid(self):
        form = make_form(first_name='')
        self.assertRaises(ValueError, form.build)


if __name__ == '__main__':
    unittest.main()
