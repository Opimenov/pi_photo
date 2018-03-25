#!/usr/bin/env python
from PIL import Image
import cStringIO
import io
import os
import smtplib
import time
import cv2
import socket
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# IMPROVEMENTS:
# log every error that occured along with times when internet connection was good
# once a week send this log over email for maintanence


def have_internet(host="8.8.8.8", port=53, timeout=3):
    """
    HOST: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    print 'checking internet'
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host,port))
        return True
    except Exception as ex:
        print ex.message + " no connection. "
        return False

def take_picture(path="/home/alex/Downloads/photo.png"):
    try:
        camera = cv2.VideoCapture(0)
        time.sleep(0.1)
        ret_val,image = camera.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image_memo = cStringIO.StringIO()
        image.save(image_memo,"PNG")
        mime_image = MIMEImage(image_memo.getvalue())
        image_memo.close()
        del(camera)
        return mime_image
    except Exception as ex:
        print ex.message + " failed to take picture. "

def send_mail(image):
    From = 'ghana.sms.project@gmail.com'
    To   = 'pialgi@live.com'
    msg = MIMEMultipart()
    msg['Subject'] = 'this is a test picture'
    msg['From'] = From
    msg['To'] = To
    text = MIMEText("test sending photo")
    msg.attach(text)
    msg.attach(image)

    #SMTP server 
    server = 'smtp.gmail.com:587'
    user_name = "ghana.sms.project@gmail.com"
    user_password = "ghanasmsproject"
    s = smtplib.SMTP(server)
    s.starttls()
    s.login(user_name, user_password)
    s.sendmail(From, To, msg.as_string())
    s.quit()

if __name__ == '__main__':
    MAX_TRIES = 20
    tried = 0
    while tried < MAX_TRIES:
        if have_internet():
            send_mail(take_picture())
            break
        else:
            tried = triepd + 1
            print "waiting"
            time.sleep(5)
    #os.system("poweroff")
        
        

