from cgitb import html
import smtplib
import ssl
from email.message import EmailMessage
from tkinter import E
from dotenv import load_dotenv
from pathlib import Path
import os
from HtmlReplaceAPI import html


load_dotenv()
env_path = "EmailSenderInfo.env"
load_dotenv(dotenv_path=env_path)
Sender = os.getenv("SenderEmail")
apppassword = os.getenv("Password")





def send_email(subject, message, to):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = Sender
    receiver_email = to
    password = apppassword
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg.set_content(message)
            
            msg.add_alternative(html, subtype="html")
            server.send_message(msg)
            print('email sent!')
        except Exception as e:
            print(e)


send_email("hello", "HII", "wolf1127r2d2@gmail.com")