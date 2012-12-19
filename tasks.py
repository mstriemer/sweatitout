import os
import smtplib
from email.mime.text import MIMEText

from sqlalchemy.sql.expression import cast

from database import db_session
from models import Registration


def email_registration_notices():
    registrations = Registration.created_yesterday(db_session).all()
    if not registrations:
        return

    body_lines = ["The following registrations were created yesterday:", ""]
    for registration in registrations:
        formatter = (" * {first_name} {last_name} {email} {phone}"
                     " - paying by {payment_type}")
        as_string = formatter.format(
                first_name=registration.first_name,
                last_name=registration.last_name,
                email=registration.email,
                phone=registration.phone,
                payment_type=registration.payment_type)
        body_lines.append(as_string)

    msg = MIMEText("\n".join(body_lines))
    msg['Subject'] = "[Sweat It Out] Yesterday's Registrations"
    msg['From'] = os.environ['EMAIL_ADDRESS']
    msg['To'] = "info@sweatitoutfit.com"

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
    smtp.sendmail(msg['From'], msg['To'], str(msg))
    smtp.close()
