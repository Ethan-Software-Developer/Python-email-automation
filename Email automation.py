import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = None

    try:
        print("Connecting to the server...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Changed to SSL
        print("Logging in...")
        server.login(sender_email, sender_password)
        print("Sending email...")
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and password.")
    except smtplib.SMTPConnectError:
        print("Error: Unable to connect to the SMTP server. Check your internet connection.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if server is not None:
            server.quit()

if __name__ == "__main__":
    sender_email = 'ethansevenster621@gmail.com'
    sender_password = 'Deadpool2006'  # Your actual password
    recipient_email = 'ethansevenster5@gmail.com'
    subject = 'Automated Email'
    body = 'This is an automated email sent from Python!'

    send_email(sender_email, sender_password, recipient_email, subject, body)
