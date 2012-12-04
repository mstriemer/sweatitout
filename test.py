import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import RegistrationForm, Base


class TestRegistrationFormValid(unittest.TestCase):
    def form(self, first_name="Bob", last_name="Smith",
            email="bob.smith@gmail.com", phone="204-555-1234",
            course_slug="the-course"):
        return RegistrationForm(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                course_slug="the-course")

    def test_valid(self):
        form = self.form()
        self.assertTrue(form.valid())

    def test_first_name_required(self):
        form = self.form(first_name='')
        self.assertFalse(form.valid())

    def test_last_name_required(self):
        form = self.form(last_name='')
        self.assertFalse(form.valid())

    def test_email_required(self):
        form = self.form(email='')
        self.assertFalse(form.valid())

    def test_phone_required(self):
        form = self.form(phone='')
        self.assertFalse(form.valid())

    def test_invalid_email_no_name(self):
        form = self.form(email='smith.com')
        self.assertFalse(form.valid())

    def test_invalid_email_no_tld(self):
        form = self.form(email='bob@smith')
        self.assertFalse(form.valid())

    def test_invalid_email_partial_tld(self):
        form = self.form(email='bob@smith.')
        self.assertFalse(form.valid())

    def test_invalid_email_partial_name(self):
        form = self.form(email='@smith.com')
        self.assertFalse(form.valid())

    def test_invalid_email_no_domain(self):
        form = self.form(email='bob@.smith')
        self.assertFalse(form.valid())

    def test_invalid_email_multiple_ats(self):
        form = self.form(email='bob@smith@gmail.com')
        self.assertFalse(form.valid())

    def test_invalid_phone_number_too_short(self):
        form = self.form(phone='5551234')
        self.assertFalse(form.valid())

    def test_invalid_phone_number_other_characters(self):
        form = self.form(phone='--\\//..  .204----11..  ')
        self.assertFalse(form.valid())


class TestRegistrationFormSave(unittest.TestCase):
    def form(self, first_name="Bob", last_name="Smith",
            email="bob.smith@gmail.com", phone="204-555-1234",
            course_slug="the-course"):
        return RegistrationForm(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                course_slug=course_slug)

    def test_build_returns_a_saveable_registration(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        form = self.form()
        registration = form.build()
        self.assertIs(registration.id, None)
        session = Session()
        session.add(registration)
        session.commit()
        self.assertEqual(registration.id, 1)

    def test_build_raises_an_exception_when_invalid(self):
        form = self.form(first_name='')
        self.assertRaises(ValueError, form.build)

if __name__ == '__main__':
    unittest.main()
