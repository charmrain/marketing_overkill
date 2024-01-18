import win32com.client

# List to store sent emails information
sent_emails_info = []

# Read HTML content outside the function
with open(r'C:\Project\7. New tech\codesite\marketing_overkill\mail\html folder\start from zero\test2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

def mail_sent(receiver):
    global sent_emails_info

    try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.To = receiver
        mail.Subject = 'EPI 2 services promotion'

        mail.HTMLBody = html_content

        # Send the email
        mail.Send()

        # Record sent email information
        sent_emails_info.append({'receiver': receiver, 'status': 'Sent'})

    except Exception as e:
        # Handle exceptions, log the information, and continue
        sent_emails_info.append({'receiver': receiver, 'status': f'Error: {str(e)}'})
