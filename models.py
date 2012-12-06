import string

from sqlalchemy import Column, Integer, String

from database import Base


class Course(object):
    def __init__(self, slug, name, description, weekdays, start_date, end_date,
            start_time, end_time, location):
        self.slug = slug
        self.name = name
        self.description = description
        self.weekdays = weekdays
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.location = location


class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    course_slug = Column(String(25), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(75), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)

class RegistrationForm(object):
    fields = [
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('email', 'Email address'),
        ('phone', 'Phone number'),
    ]
    hidden_fields = [
        ('course_slug', 'Course slug'),
    ]

    def __init__(self, **kwargs):
        self._valid = True

        _fields = self.fields
        self.fields = []
        self.fields_by_name = {}
        for field in _fields:
            form_field = FormField(field[0], field[1], kwargs.get(field[0], ''))
            self.fields.append(form_field)
            self.fields_by_name[field[0]] = form_field
        _hidden_fields = self.hidden_fields
        self.hidden_fields = []
        for field in _hidden_fields:
            form_field = FormField(field[0], field[1], kwargs.get(field[0], ''))
            self.hidden_fields.append(form_field)
        self.all_fields = self.hidden_fields + self.fields


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
        return Registration(**{f.name: f.value for f in self.all_fields})

    def _validate_presence(self, field):
        form_field = self.fields_by_name[field]
        field_valid = bool(form_field.value)
        if not field_valid:
            form_field.errors.append('required')
        self._valid = self._valid and field_valid

    def _validate_email(self, field):
        form_field = self.fields_by_name[field]
        email = form_field.value
        field_valid = (
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
        if not field_valid:
            form_field.errors.append('not a valid email')
        self._valid = self._valid and field_valid

    def _validate_phone(self, field):
        form_field = self.fields_by_name[field]
        digit_count = 0
        for letter in form_field.value:
            if letter in string.digits:
                digit_count += 1
            if digit_count >= 10:
                break
        field_valid = digit_count >= 10
        if not field_valid:
            form_field.errors.append('at least 10 digits are required')
        self._valid = self._valid and field_valid


class FormField(object):
    def __init__(self, name, description, value=''):
        self.name = name
        self.description = description
        self.value = value
        self.errors = []
