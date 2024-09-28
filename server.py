from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Replace with your email and app password
EMAIL = "vgboss91@gmail.com"
PASSWORD = "no_option"

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
