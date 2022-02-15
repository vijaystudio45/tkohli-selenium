import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key="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")
from_email = Email("nitinkatochstudio45@gmail.com")  # Change to your verified sender
to_email = To("tosharstudio45@gmail.com")  # Change to your recipient
subject = "This is jenking Email sending from tushar saini"
content = Content("text/plain", "Sendgrid Email successfully send from tushar saini")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
if response.status_code == 202:
    print('Email send successfully')
else:
    print('Email send successfully not send')