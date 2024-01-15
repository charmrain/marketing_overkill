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
    <p>Raymond</p>

    <!-- Simple Picture -->
    <img src="https://placekitten.com/300/200" alt="Greeting Image">

    <!-- Hyperlink to Google -->
    <p>Check out <a href="https://www.google.com" target="_blank">Google</a> for more!</p>

</body>
</html>

"""


html_2 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            margin-top: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<table>
    <tr>
        <th>Picture</th>
        <th>Text Content</th>
    </tr>
    <tr>
        <td><img src="https://placekitten.com/150/100" alt="Image 1"></td>
        <td>
            <p>This is the first row of text content.</p>
            <p>Here's the second sentence.</p>
            <p>A third sentence for more information.</p>
            <p>Adding a fourth sentence to the mix.</p>
            <p>This is the fifth and final sentence.</p>
            <button class="button" onclick="alert('Button Clicked!')">Click me</button>
        </td>
    </tr>
    <tr>
        <td><img src="https://placekitten.com/150/100" alt="Image 2"></td>
        <td>
            <p>This is another set of text for the second row.</p>
            <p>Adding more details in the second sentence.</p>
            <p>Third sentence for additional context.</p>
            <p>The fourth sentence provides more insights.</p>
            <p>Here's the fifth sentence in this row.</p>
            <button class="button" onclick="alert('Button Clicked!')">Click me</button>
        </td>
    </tr>
    <tr>
        <td><img src="https://placekitten.com/150/100" alt="Image 3"></td>
        <td>
            <p>Text content for the third row begins here.</p>
            <p>Second sentence for the third row.</p>
            <p>Third sentence for more details.</p>
            <p>Fourth sentence to elaborate further.</p>
            <p>The fifth sentence concludes this row.</p>
            <button class="button" onclick="alert('Button Clicked!')">Click me</button>
        </td>
    </tr>
</table>

</body>
</html>
"""

import win32com.client as win32

# Load HTML content from file
with open(r'C:\Project\7. New tech\codesite\marketing_overkill\mail\robertHalf.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# below is the first version 

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'raymond@epi2services.com'
mail.Subject = 'EPI 2 services promotion for Raymond'

mail.HTMLBody = html_content

mail.Send()