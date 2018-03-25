#!/usr/bin/env python

import os
import smtplib
import time
import cv2
import socket
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# TODO:
# take a picture
# save it
# check internet connection
# if available send email
# else wait for some time

EMAIL_SENT = False

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
        print ex.message + "no connection"
        return False

def take_picture(path="/home/alex/Downloads/photo.png"):
    print "taking picture"
    camera = cv2.VideoCapture(0)
    time.sleep(0.1)
    return_value, image = camera.read()
    cv2.imwrite(path, image) #writes an image to disk
    del(camera)

def send_mail(file_path="/home/alex/Downloads/photo.png"):
    From = 'ghana.sms.project@gmail.com'
    #print 'From' + From
    To   = 'pialgi@live.com' #'andrew_exe@hotmail.com'
    #print 'To' + To
    #email content 
    img_data = open(file_path, 'rb').read()
    #print 'opened image'
    msg = MIMEMultipart()
    msg['Subject'] = 'this is a test picture'
    #print 'subject setup'
    msg['From'] = From
    msg['To'] = To
    text = MIMEText("test sending photo")
    msg.attach(text)
    #print 'attached text'
    image = MIMEImage(img_data, name=os.path.basename(file_path))
    msg.attach(image)
    #print 'attached image'

    #SMTP server 
    server = 'smtp.gmail.com:587'
    user_name = "ghana.sms.project@gmail.com"
    user_password = "ghanasmsproject"
    s = smtplib.SMTP(server)
    #print 'server created'
    s.starttls()
    s.login(user_name, user_password)
    #print 'logged in'
    s.sendmail(From, To, msg.as_string())
    print 'email sent'
    s.quit()
    EMAIL_SENT = True

if __name__ == '__main__':
    MAX_TRIES = 20
    tried = 0
    take_picture()
    while tried < MAX_TRIES:
        if have_internet():
            send_mail()
            break
        else:
            tried = triepd + 1
            print "waiting"
            time.sleep(5)
    os.system("poweroff")
        
        

