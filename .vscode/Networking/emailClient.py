# Creating an smtp client that sends out emails
# We use gmail server as smtp server
# 1. Create the message body, from to info
# 2. Create an smtp server
# 3. Once connected, login and send a message
# 4. Quit


import smtplib
from email.mime.text import MIMEText # To creat the body of the email


body = 'This is a test email, how are you?'

msg = MIMEText(body)

msg['From'] = 'saumya.jain470@gmail.com'

msg['To'] = 'saumya.jain470@gmail.com'

msg['Subject'] = 'Hello'

# Open connection

server = smtplib.SMTP('smtp.gmail.com',587) # Default port is 587
server.starttls()
server.login('saumya.jain470@gmail.com','Se@ttle@1234')
server.send_message(msg)

print('Mail sent')

server.quit()




