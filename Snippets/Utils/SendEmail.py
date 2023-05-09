import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE
from typing import List

def send_email(subject: str, message: str, from_email: str, to_emails: List[str], smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str, html: bool = False, attachments: List[str] = None):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = COMMASPACE.join(to_emails)

    if html:
        msg.attach(MIMEText(message, 'html', 'utf-8'))
    else:
        msg.attach(MIMEText(message, 'plain', 'utf-8'))

    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as file:
                part = MIMEApplication(file.read(), Name=attachment)
                part['Content-Disposition'] = f'attachment; filename="{attachment}"'
                msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_user, smtp_password)
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()
