import win32com.client
import pandas as pd

# List to store sent emails information
sent_emails_info = []

# Read HTML content outside the function
with open(r'C:\Project\7. New tech\codesite\marketing_overkill\mail\html folder\start from zero\test_Jan18.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

def mail_sent(receiver):
    global sent_emails_info

    try:
        outlook = win32com.client.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.To = receiver
        mail.Subject = 'New Year New Goal'

        mail.HTMLBody = html_content

        # Send the email
        mail.Send()

        # Record sent email information
        sent_emails_info.append({'receiver': receiver, 'status': 'Sent'})

    except Exception as e:
        # Handle exceptions, log the information, and continue
        sent_emails_info.append({'receiver': receiver, 'status': f'Error: {str(e)}'})



def send_summary_email(superviser):
    global sent_emails_info

    # Create a summary email
    outlook = win32com.client.Dispatch('Outlook.Application')
    summary_mail = outlook.CreateItem(0)
    summary_mail.To = superviser
    summary_mail.Subject = 'Email Summary Report'

    # Create the body of the summary email
    summary_body = '<p>Summary of Sent Emails:</p>'
    for email_info in sent_emails_info:
        summary_body += f"<p>To: {email_info['receiver']}, Status: {email_info['status']}</p>\n"

    # Set HTML body for the summary email
    summary_mail.HTMLBody = summary_body

    # Send the summary email
    summary_mail.Send()

    with open(r"C:\Project\7. New tech\codesite\marketing_overkill\mail\summary.txt", 'a', encoding='utf-8') as txt_file:
        txt_file.write(summary_body)




# Example of how to use the functions
# receivers_list = ['1@gmail.com', '2@gmail.com']
df = pd.read_excel(r'C:\Project\5. Marketing\Customer list\Minneapolis business_with emails.xlsx')
receivers = df['contact email'][:50]


# print(df['contact email'][:50])
# print(len(df['contact email']))
# print(len(df['contact email'][:50]))
# print(type(df['contact email'][:50]))
# print(recievers)



# Send emails and record information
for id, receiver in enumerate(receivers):
    mail_sent(receiver)
    print('email sent', id+1)



# Send the summary email after all emails are sent
send_summary_email('raymond@epi2services.com')