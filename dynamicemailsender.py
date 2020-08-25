import smtplib  # for sending mails via server
from email.message import EmailMessage  # email components
from string import Template  # to substitute
from pathlib import Path  # to read html files


html = Template(Path('index.html').read_text())

email = EmailMessage()  # email is an object of EmailMessage() class
email['from'] = 'fromname'
email['to'] = 'toemailid'
email['subject'] = 'This is a test email using python'

email.set_content(html.substitute(name='Sam'), 'html')  # 1st arg is substituting the name, 2nd arg is specifying its an html file


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # general protocol
    smtp.starttls()  # start the secure encrypted connection
    smtp.login('senderemailid', 'senderemailpassword')
    smtp.send_message(email)
print('Email has been sent successfully!')
