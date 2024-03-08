import win32com.client
import pandas as pd

# List to store sent emails information
sent_emails_info = []

# Read HTML content outside the function
with open(r'C:\Project\7. New tech\codesite\marketing_overkill\mail\html folder\start from zero\marketing_promo_march4.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

def mail_sent(receiver):
    global sent_emails_info

    try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.To = receiver
        mail.Subject = 'this is the updated version'

        mail.HTMLBody = html_content
        # mail.Importance = 2

        # Send the email
        mail.Send()

        # Record sent email information
        sent_emails_info.append({'receiver': receiver, 'status': 'Sent'})

    except Exception as e:
        # Handle exceptions, log the information, and continue
        sent_emails_info.append({'receiver': receiver, 'status': f'Error: {str(e)}'})


receivers = ['raymond@epi2services.com', 'terri@luacoffee.com', 'adriana@epi2services.com']
# 'thomas@epi2services.com', 'terri@luacoffee.com', 'trinity@epi2services.com', 'yuqing@epi2services.com', 'cuong@epi2services.com', 
# 'choua@epi2services.com', 'ly@epi2services.com']


# Send emails and record information
for id, receiver in enumerate(receivers):
    mail_sent(receiver)
    print('email sent', id+1)