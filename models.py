import string

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    course_slug = Column(String(25), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(75), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)


class RegistrationForm(object):
    def __init__(self, session_factory=None, **kwargs):
        self.kwargs = kwargs
        self._valid = True
        self.session_factory = session_factory

    def valid(self):
        presence = ['first_name', 'last_name', 'email', 'phone']
        for field in presence:
            self._validate_presence(field)

        self._validate_email('email')
        self._validate_phone('phone')
        return self._valid

    def build(self):
        if not self.valid():
            raise ValueError('form is invalid')
        return Registration(**self.kwargs)

    def _validate_presence(self, field):
        self._valid = self._valid and bool(self.kwargs.get(field, None))

    def _validate_email(self, field):
        email = self.kwargs.get(field, '')
        self._valid = (
                # have to be valid already
                self._valid and
                # there can only be one '@'
                len(email.split('@')) == 2 and
                # there needs to be a username before the '@'
                bool(email.split('@')[0]) and
                # there needs to be a '.' to split the domain and the TLD
                '.' in email.split('@')[-1] and
                # there needs to be a domain
                bool(email.split('@')[-1].split('.')[0]) and
                # there needs to be a TLD
                bool(email.split('.')[-1]))

    def _validate_phone(self, field):
        digit_count = 0
        for letter in self.kwargs.get(field, ''):
            if letter in string.digits:
                digit_count += 1
            if digit_count >= 10:
                break
        self._valid = self._valid and digit_count >= 10
