from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Replace with your email and app password
EMAIL = "vgboss91@gmail.com"
PASSWORD = "gvcr csbf shkw vrhh"

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Free Fire Tournament Registration</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f7f7f7;
                font-family: 'Arial', sans-serif;
            }
            .form-container {
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
                padding: 30px;
                max-width: 500px;
                margin: 50px auto;
            }
            .form-container h2 {
                text-align: center;
                margin-bottom: 30px;
                color: #333;
            }
            .form-container button {
                width: 100%;
                background-color: #007bff;
                color: #fff;
                border: none;
                padding: 15px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            .form-container button:hover {
                background-color: #0056b3;
            }
            footer {
                text-align: center;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="form-container">
                <h2>Free Fire Tournament Registration</h2>
                <form id="registrationForm" method="POST" action="/register">
                    <div class="mb-3">
                        <label for="id_name" class="form-label">ID Name</label>
                        <input type="text" class="form-control" name="id_name" id="id_name" placeholder="Enter your ID Name" required>
                    </div>
                    <div class="mb-3">
                        <label for="game_uid" class="form-label">Game UID</label>
                        <input type="text" class="form-control" name="game_uid" id="game_uid" placeholder="Enter your Game UID" required>
                    </div>
                    <div class="mb-3">
                        <label for="squad_name" class="form-label">Squad Name</label>
                        <input type="text" class="form-control" name="squad_name" id="squad_name" placeholder="Enter your Squad Name" required>
                    </div>
                    <button type="submit">Submit Registration</button>
                </form>
            </div>
        </div>
        <footer>
            Free Fire Tournament Registration &copy; 2024
        </footer>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''

def send_email(id_name, game_uid, squad_name):
    # Email configuration
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = "nmesportsofficial1@gmail.com"  # New recipient email
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
        server.sendmail(EMAIL, "nmesportsofficial1@gmail.com", text)
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
    
    if send_email(id_name, game_uid, squad_name):
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
            <title>Registration Successful</title>
        </head>
        <body>
            <div class="container mt-5">
                <div class="alert alert-success" role="alert">
                    Registration Successful! A confirmation email has been sent.
                </div>
            </div>
        </body>
        </html>
        '''
    else:
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
            <title>Registration Failed</title>
        </head>
        <body>
            <div class="container mt-5">
                <div class="alert alert-danger" role="alert">
                    Registration Failed! Unable to send email.
                </div>
            </div>
        </body>
        </html>
        '''

if __name__ == '__main__':
    app.run(debug=True)
