import smtplib
import ssl
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = "smtp.gmail.com"
owner_email = "your@gmail.com"
owner_password = "write your app key"

def generate_otp():
    return ''.join(random.choices(string.digits, k=4))

def send_email(receiver_email, otp, activation_link):
    context = ssl.create_default_context()

    with open("index.html", "r") as file:
        html_template = file.read()

    html_content = html_template.replace("{{ activation_code }}", otp)
    html_content = html_content.replace("{{ activation_link }}", activation_link)

    message = MIMEMultipart("alternative")
    message["From"] = owner_email
    message["To"] = receiver_email
    message["Subject"] = "Your OTP Code"

    plain_text = f"Your OTP code is: {otp}\n\nUse the following link if needed: {activation_link}"
    message.attach(MIMEText(plain_text, "plain"))
    message.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(smtp_server, port) as mail:
            mail.ehlo()
            mail.starttls(context=context)
            mail.login(owner_email, owner_password)
            mail.sendmail(owner_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    receiver_email = input("Enter the recipient's email address: ")
    if not receiver_email:
        print("Email address is required.")
    elif not "@" in receiver_email:
        print("Email is not correct format")
    else:
        otp = generate_otp()
        activation_link = "https://example.com/activate" 
        send_email(receiver_email, otp, activation_link)
        print(f"OTP sent to {receiver_email}: {otp}")
