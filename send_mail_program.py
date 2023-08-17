import os
import time

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
messages="driver drowsiness alert at "+ str(current_time)
#print(messages)

def send_email(mId,im):

        fromaddr = 'drowsinessalert000@gmail.com'
        toaddrs  = str(mId)
        msg = MIMEMultipart()

        text = MIMEText(messages)
        msg['Subject'] = 'NOTIFICATION ALERT'
        msg.attach(text)
        img_data = open(str(im), 'rb').read()
        image = MIMEImage(img_data,name=im)
        msg.attach(image)

        # Credentials (if needed)
        username = 'drowsinessalert000@gmail.com'
        password = 'Qwerty@12345'

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
        print('e-Mail Sent')




