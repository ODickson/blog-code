from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import json


email_secrets_path = "email_secrets.json"
with open(email_secrets_path) as f:
    email_secrets = json.load(f)

def send_email(subject:str, body:str, email_secrets = email_secrets,recipients:list=['o.b.p.dickson@live.com']):
    """
    Sends an email to a list of recipients.

    Args:
        recipients (list): A list of email addresses to send the email to.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """


    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = email_secrets['email_address']
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    msg_full = msg.as_string()

    with smtplib.SMTP("smtp.gmail.com", 587) as S:
        S.ehlo()
        S.starttls()
        S.ehlo()
        S.login(email_secrets['email_address'], email_secrets['client_secret'])
        S.sendmail(email_secrets['email_address'],
                    ",".join(recipients),
                    msg_full)
        S.quit()