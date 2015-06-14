import string
from datetime import datetime
from time import time

from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey, Boolean,
                        func)
from sqlalchemy.orm import relationship

from database import Base

COURSE_SLUG_MAX_LENGTH = 25


class Course(object):
    def __init__(self, slug=None, name=None, description=None, days=[],
                 start_date=None, end_date=None, location=None, cost=None,
                 has_space=None, map_image=None, map_url=None,
                 map_embed_url=None, drop_in_open=False, drop_in_fee=None,
                 note=None, partial_attendance=False, allow_assessments=False):
        if len(slug) > COURSE_SLUG_MAX_LENGTH:
            raise ValueError('slug must be {length} characters or less'.format(
                length=COURSE_SLUG_MAX_LENGTH))
        self.slug = slug
        self.name = name
        self.description = description
        self.days = [Day(*day) for day in days]
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.cost = cost
        self.has_space = has_space
        self.map_image = map_image
        self.map_url = map_url
        self.map_embed_url = map_embed_url
        self.drop_in_open = drop_in_open
        self.drop_in_fee = drop_in_fee
        self.note = note
        self.partial_attendance = partial_attendance
        self.allow_assessments = allow_assessments

    @property
    def costs(self):
        costs = [self.cost]
        costs.extend([day.cost for day in self.days if day.cost is not None])
        return sorted(set(costs), reverse=True)

    def same_time_each_day(self):
        prev_day = self.days[0]
        for day in self.days[1:]:
            if not prev_day.same_time_as(day):
                return False
            prev_day = day
        return True

    def day(self, name):
        for day in self.days:
            if day.name.lower() == name.lower():
                return day
        else:
            raise KeyError('{name} is not a valid day'.format(name=name))

    def completed(self):
        return self.end_datetime < datetime.today()

    def upcoming(self):
        return self.start_datetime > datetime.today()

    @property
    def end_datetime(self):
        return parse_human_date(self.end_date)

    @property
    def start_datetime(self):
        return parse_human_date(self.start_date, year_fallback=self.end_date)


class Day(object):
    def __init__(self, name, start_time, end_time, cost=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.cost = cost

    def same_time_as(self, other):
        return (self.start_time == other.start_time and
                self.end_time == other.end_time)


def _make_registration_code(context):
    row_seed = ''
    row_seed += context.current_parameters['first_name']
    row_seed += context.current_parameters['last_name']
    row_seed += context.current_parameters['course_slug']
    seed = int(time())
    for c in row_seed:
        seed += ord(c)
    return "{:x}".format(seed % (16 ** 4)).rjust(4, '0')


class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), nullable=False, default=_make_registration_code)
    registration_date = Column(DateTime, nullable=False, default=func.now())
    course_slug = Column(String(COURSE_SLUG_MAX_LENGTH), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(75), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    payment_type = Column(String(10), nullable=False)
    paypal_email = Column(String(255))
    stripe_card_token = Column(String(255))
    registration_charge = relationship("RegistrationCharge", uselist=False,
                                       backref="registration")
    attendance = Column(String(25), nullable=False, default='both')
    referrer_name = Column(String(255))
    assessments = Column(Boolean, nullable=False, default=False)

    @property
    def descriptive_payment_type(self):
        return {
            'paypal': "PayPal",
            'in_person': "In person",
            'stripe': "Stripe",
        }[self.payment_type]

    def __str__(self):
        template = (
            "{course_slug}: "
            "{first_name} {last_name} ({email}) - "
            "{payment_type}")
        return template.format(
            course_slug=self.course_slug, first_name=self.first_name,
            last_name=self.last_name, payment_type=self.payment_type,
            email=self.email)

    def __repr__(self):
        return "<Registration: " + str(self) + ">"


class RegistrationCharge(Base):
    __tablename__ = 'registration_charges'

    id = Column(Integer, primary_key=True)
    registration_id = Column(Integer, ForeignKey('registrations.id'),
                             nullable=False)
    stripe_charge_token = Column(String(255))
    paid = Column(Boolean, nullable=False)
    last4 = Column(String(4))
    card_type = Column(String(25))
    currency = Column(String(3))
    amount = Column(Integer)
    fee = Column(Integer)
    charge_time = Column(DateTime)
    error_code = Column(String(30))


def attendance_options(field):
    return ([('both', 'Both ${cost}'.format(cost=field.form.instance.cost))] +
            [(day.name.lower(), '{day} ${cost}'.format(day=day.name,
                                                       cost=day.cost))
             for day in field.form.instance.days])


class RegistrationForm(object):
    fields = [
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('email', 'Email address'),
        ('phone', 'Phone number'),
        ('referrer_name', 'Referrer\'s full name', {'required': False}),
        ('attendance', 'Days', {
            'options': attendance_options,
            'show_if': lambda field: field.form.instance.partial_attendance,
        }),
        ('assessments',
         'Track your results with accountability assessments ($20)',
         {
             'checkbox': True,
             'show_if': lambda field: field.form.instance.allow_assessments,
         }),
        ('payment_type', 'Payment type', {
            'options': [
                ['paypal', 'PayPal'],
                ['in_person', 'In person'],
            ]
        }),
    ]
    hidden_fields = [
        ('course_slug', 'Course slug'),
        ('paypal_email', 'PayPal email address'),
    ]

    def __init__(self, **kwargs):
        self._valid = True

        self.instance = kwargs.get('instance')

        _fields = self.fields
        self.fields = []
        self.fields_by_name = {}
        for field in _fields:
            extra = field[2] if len(field) > 2 else {}
            form_field = FormField(self, field[0], field[1],
                                   kwargs.get(field[0], ''), **extra)
            if form_field.show():
                self.fields.append(form_field)
            self.fields_by_name[field[0]] = form_field
        _hidden_fields = self.hidden_fields
        self.hidden_fields = []
        for field in _hidden_fields:
            form_field = FormField(self, field[0], field[1],
                                   kwargs.get(field[0], ''))
            self.hidden_fields.append(form_field)
            self.fields_by_name[field[0]] = form_field
        self.all_fields = self.hidden_fields + self.fields

    def valid(self):
        presence = ['first_name', 'last_name', 'email', 'phone']
        for field in presence:
            self._validate_presence(field)
        self._validate_options('attendance')
        self._validate_options('payment_type')
        self._validate_email('email')
        self._validate_phone('phone')

        payment_type = self.fields_by_name['payment_type']
        if payment_type.value == 'paypal':
            self._validate_presence('paypal_email')
            self._validate_email('paypal_email')

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

    def _validate_options(self, field):
        form_field = self.fields_by_name[field]
        if form_field.show():
            field_valid = form_field.value in form_field.valid_options
            if not field_valid:
                form_field.errors.append('not a valid option')
            self._valid = self._valid and field_valid


class FormField(object):
    def __init__(self, form, name, description, value='', options=None,
                 show_if=None, required=True, checkbox=False):
        self.form = form
        self.name = name
        self.description = description
        self.checkbox = checkbox
        self.options = options(self) if callable(options) else options or []
        self.valid_options = [o[0] for o in self.options or []]
        self.show_if = show_if
        self.errors = []
        self.required = required
        if self.checkbox:
            self.value = value == '1'
        else:
            self.value = value

    def show(self):
        if callable(self.show_if):
            return self.show_if(self)
        else:
            return True


def parse_human_date(date_string, year_fallback=None):
    suffices = ['st', 'nd', 'rd', 'th']
    parsed = None
    # If date_string doesn't have a year, use the year from year_fallback.
    if ',' not in date_string and ',' in year_fallback:
        date_string += ',' + year_fallback.split(',', 1)[1]
    for suffix in suffices:
        try:
            parsed = datetime.strptime(
                date_string, '%B %d{suffix}, %Y'.format(suffix=suffix))
            break
        except ValueError:
            pass
    if parsed is None:
        raise ValueError("could not parse {} to datetime".format(date_string))
    return parsed


class ProgramDesignRegistration(Base):
    __tablename__ = 'program_design_registration'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    trainer = Column(String(255))
    package = Column(String(255))
    registration_date = Column(DateTime)

    @property
    def trainer_email(self):
        return self.trainer.lower() + '@sweatitoutfit.com'
