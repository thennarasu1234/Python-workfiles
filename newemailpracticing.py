# IMPORTANT: For Gmail, use an App Password, not your regular password.
# See: https://support.google.com/accounts/answer/185833

import smtplib

recipient_email = "thenn9342@gmail.com.com"
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