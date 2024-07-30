import requests
import smtplib
import time
import asyncio
import random
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

users_list = [] 
files = ["pmail1.html", "pmail2.html", "pmail3.html", "pmail4.html", "pmail5.html", 
         "pmail6.html", "pmail7.html", "pmail8.html", "pmail9.html", "pmail10.html"]

user = input("Please enter a UserMail:")
file_input = input("Please enter a filename for phishing:")

port = 587
smtp_server = "smtp.gmail.com"
owner_mail = "your@gmail.com"
owner_password = "YOUR APP KEY"

def send_mail(reciever_email):
    context = ssl.create_default_context()
    with open(file_input,"r") as f:
        content = f.read()
        message = MIMEMultipart("alternative")
    message["From"] = owner_mail
    message["To"] = reciever_email
    message["Subject"] = "Your OTP Code"

    #plain_text = f"Your OTP code is: {otp}\n\nUse the following link if needed: {activation_link}"
    #message.attach(MIMEText(plain_text, "plain"))
    message.attach(MIMEText(content, "html"))

    try:
        with smtplib.SMTP(smtp_server, port) as mail:
            mail.ehlo()
            mail.starttls(context=context)
            mail.login(owner_mail, owner_password)
            mail.sendmail(owner_mail, reciever_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    #receiver_email = input("Enter the recipient's email address: ")
    send_mail(user)

        #print(f"OTP sent to {receiver_email}: {otp}")

#server = smtplib.SMTP()
