from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Replace with your email and app password
EMAIL = "vgboss91@gmail.com"
PASSWORD = "gvcr csbf shkw vrhh"

# HTML Templates in Python strings
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Fire Tournament Registration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .registration-form {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px #ccc;
            max-width: 400px;
            width: 100%;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="registration-form">
        <h2>Register for Tournament</h2>
        <form action="/register" method="POST">
            <div class="mb-3">
                <label for="id_name" class="form-label">ID Name</label>
                <input type="text" class="form-control" id="id_name" name="id_name" required>
            </div>
            <div class="mb-3">
                <label for="game_uid" class="form-label">Game UID</label>
                <input type="text" class="form-control" id="game_uid" name="game_uid" required>
            </div>
            <div class="mb-3">
                <label for="squad_name" class="form-label">Squad Name</label>
                <input type="text" class="form-control" id="squad_name" name="squad_name" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Submit</button>
        </form>
    </div>
</body>
</html>
"""

success_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Successful</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #d4edda;
        }
        .success-message {
            text-align: center;
            padding: 30px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px #ccc;
        }
    </style>
</head>
<body>
    <div class="success-message">
        <h2>Registration Successful!</h2>
        <p>Thank you for registering for the tournament.</p>
    </div>
</body>
</html>
"""

failure_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Failed</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f8d7da;
        }
        .failure-message {
            text-align: center;
            padding: 30px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px #ccc;
        }
    </style>
</head>
<body>
    <div class="failure-message">
        <h2>Registration Failed</h2>
        <p>We encountered an error while processing your registration. Please try again.</p>
    </div>
</body>
</html>
"""

# Email sending function
def send_email(id_name, game_uid, squad_name):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = "nmesportsofficial1@gmail.com"
    msg['Subject'] = "New Free Fire Tournament Registration"

    # Email content
    body = f"""
    New Registration Details:

    ID Name: {id_name}
    Game UID: {game_uid}
    Squad Name: {squad_name}
    """
    msg.attach(MIMEText(body, 'plain'))

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

@app.route('/')
def home():
    return render_template_string(index_html)

@app.route('/register', methods=['POST'])
def register():
    id_name = request.form.get('id_name')
    game_uid = request.form.get('game_uid')
    squad_name = request.form.get('squad_name')

    # Validate that Game UID is a number
    if not game_uid.isdigit():
        return "Game UID must be a number."

    # Send the email and return the appropriate page
    if send_email(id_name, game_uid, squad_name):
        return render_template_string(success_html)
    else:
        return render_template_string(failure_html)

if __name__ == '__main__':
    app.run(debug=True)
