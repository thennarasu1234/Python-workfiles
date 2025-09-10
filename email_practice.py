# IMPORTANT: For Gmail, use an App Password, not your regular password.
# See: https://support.google.com/accounts/answer/185833

import smtplib

recipient_email = "rab874972@gmail.com"
sender_email = "thennarasut415@gmail.com"  # Use full email address
app_password = "elix yfvm ippo aabs"  # Replace with your Gmail App Password

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(sender_email, app_password)
message = "Hello from Python"
smtp_server.sendmail(sender_email, recipient_email, message)
smtp_server.quit()

list_1=["rab874972@gmail.com","prnirmalramesh04@gmail.com","quintaranino03@gmail.com"]

message="hey there"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,app_password)
for i in list_1:
    server.sendmail(sender_email,i,message)
server.quit()


# IMPORTANT: For Gmail, use an App Password, not your regular password.
# See: https://support.google.com/accounts/answer/185833

import smtplib

recipient_email = "thenn469142@gmail.com"
sender_email = "thennarasut415@gmail.com"
app_password = "crwr nzby chsi metj"   # Replace with your Gmail App Password

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls() 
smtp_server.login(sender_email,app_password)
message = "I am Thenn"
smtp_server.sendmail(sender_email, recipient_email, message)
smtp_server.quit()

# Example: Sending an email with a file attachment
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = "thennarasut415@gmail.com"
recipient_email = "rab874972@gmail.com"
app_password = "your_app_password_here"  # Use your Gmail App Password
subject = "Subject: Sending Attachment"
body = "This email contains an attachment."
filename = "example.txt"  # Path to the file you want to attach

# Create a multipart message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Open file in binary mode and attach
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
msg.attach(part)

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(sender_email, app_password)
smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
smtp_server.quit()
