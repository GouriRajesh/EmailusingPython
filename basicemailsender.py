import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'fromname'
email['to'] = 'toemailid'
email['subject'] = 'This is a test email using python'
email.set_content('I have sent this email using python!! I\'m so happyyyyy')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('senderemailid', 'senderemailpassword')
    smtp.send_message(email)
print('Email has been sent successfully!')