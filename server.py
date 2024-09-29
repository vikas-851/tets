from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Replace with your email and app password
EMAIL = "your-email@gmail.com"
PASSWORD = "your-app-password"

# Serve the HTML form at the root URL
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Free Fire Tournament Registration</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .registration-form {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 300px;
            }
            .registration-form h2 {
                margin-bottom: 20px;
                text-align: center;
            }
            .registration-form input[type="text"], .registration-form input[type="number"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .registration-form button {
                width: 100%;
                padding: 10px;
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .registration-form button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="registration-form">
            <h2>Tournament Registration</h2>
            <form id="registrationForm" method="POST" action="/register">
                <input type="text" name="id_name" placeholder="ID Name" required>
                <input type="text" name="game_uid" placeholder="Game UID" required>
                <input type="text" name="squad_name" placeholder="Squad Name" required>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    '''

def send_email(id_name, game_uid, squad_name):
    # Email configuration
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg['Subject'] = "New Free Fire Tournament Registration"
    
    # Email content
    body = f"""
    New Registration Details:
    
    ID Name: {id_name}
    Game UID: {game_uid}
    Squad Name: {squad_name}
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Sending email via Gmail SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL, EMAIL, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/register', methods=['POST'])
def register():
    id_name = request.form.get('id_name')
    game_uid = request.form.get('game_uid')
    squad_name = request.form.get('squad_name')
    
    # Send email with the registration details
    if send_email(id_name, game_uid, squad_name):
        return "Registration Successful! Email sent."
    else:
        return "Registration Failed! Unable to send email."

if __name__ == '__main__':
    app.run(debug=True)
