import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your email credentials
sender_email = 'info@epi2services.com'
sender_password = 'if_c_lakes2023'
receiver_email = 'raymond@epi2services.com'

# Create the MIME object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Subject of the email'

# Add the email body
body = 'This is the body of the email.'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server (in this case, Gmail's SMTP server)
with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
    server.starttls()
    
    # Login to the email account
    server.login(sender_email, sender_password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Email sent successfully!')