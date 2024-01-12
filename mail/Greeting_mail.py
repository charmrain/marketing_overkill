html_contents = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting Letter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Warm Greetings!</h1>
    <p>Dear Terri,</p>
    <p>Wishing you a fantastic day filled with joy and laughter. May this day bring you happiness and success in all your endeavors.</p>
    <p>Best regards,</p>
    <p>Your Name</p>

    <!-- Simple Picture -->
    <img src="https://placekitten.com/300/200" alt="Greeting Image">

    <!-- Hyperlink to Google -->
    <p>Check out <a href="https://www.google.com" target="_blank">Google</a> for more!</p>

</body>
</html>

"""

import win32com.client as win32

# below is the first version 

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'raymond@epi2services.com'
mail.Subject = 'a new test'

mail.HTMLBody = html_contents

mail.Send()