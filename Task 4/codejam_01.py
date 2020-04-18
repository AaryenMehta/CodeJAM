from tkinter import *
import json
import smtplib
from email.mime.text import MIMEText

bgrp = ''
mailing_list = []
len = 0
flag = 0

def printtext():
    btn.destroy()
    
    lbl3 = Label(window,text="Database has been searched")
    lbl3.pack()
    
    global e
    global bgrp
    global len
    
    bgrp = e.get()
    
    f = open("/home/aaryen/Desktop/ERA-IITK/task5/students.json") 
    data = json.load(f) 
    
    for i in data: 
        if bgrp == 'A+':
            if i['b'] == 'A+' or i['b'] == 'A-' or i['b'] == 'O+' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'A-':
            if i['b'] == 'A-' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'B+':
            if i['b'] == 'B+' or i['b'] == 'B-' or i['b'] == 'O+' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'B-':
            if i['b'] == 'B-' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'AB+':
            if i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'AB-':
            if i['u'] == 'AB-' or i['u'] == 'A-' or i['u'] == 'B-' or i['u'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'O+':
            if i['u'] == 'O+' or i['u'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'O-':
            if i['u'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
    
    f.close()
    
    print("ALERT:", len, "people who can donate to", bgrp,"blood group have been found")
    
    return

def sendmail():
    btn2.destroy()
    
    lbl2 = Label(window,text="Congratulations! Emails have been sent")
    lbl2.pack()
    global e
    global bgrp
    global len
    
    bgrp = e.get()
    #print(bgrp)
    
    f = open("/home/aaryen/Desktop/ERA-IITK/task5/students.json") 
    data = json.load(f) 
    
    for i in data: 
        if bgrp == 'A+':
            if i['b'] == 'A+' or i['b'] == 'A-' or i['b'] == 'O+' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'A-':
            if i['b'] == 'A-' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'B+':
            if i['b'] == 'B+' or i['b'] == 'B-' or i['b'] == 'O+' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'B-':
            if i['b'] == 'B-' or i['b'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'AB+':
            if i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'AB-':
            if i['u'] == 'AB-' or i['u'] == 'A-' or i['u'] == 'B-' or i['u'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'O+':
            if i['u'] == 'O+' or i['u'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1
        elif bgrp == 'O-':
            if i['u'] == 'O-' and i['u'] != '':
                mailing_list.append(i['u']+"@iitk.ac.in")
                len += 1     
    
    f.close()
    
    s = smtplib.SMTP('mmtp.iitk.ac.in') #smtp server of iitk
    s.set_debuglevel(1)
    
    msg = MIMEText("Respected Sir/Madam,\nThere is an urgent requirement for blood in the HC for Mr.Mukesh. Please contact Dr. Mohan for further details.")
    sender = 'ammehta@iitk.ac.in'
    recipients = []
    #uncomment the below line if you want to send the mail
    #recipients = mailing_list 
    
    msg['Subject'] = "URGENT: Blood Required"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    
    s.sendmail(sender, recipients, msg.as_string())
    
    print("ALERT:",len,"people who can donate to",bgrp,"blood group have been notified of your email")
    
    return

if __name__ == '__main__':
    
    window = Tk()
    window.geometry("240x240")
    window.title("Blood Donation")
    
    lbl = Label(window,text="Enter Blood Group Here")
    lbl.pack()
    
    e = Entry(window)
    e.pack()
    e.focus_set()
    
    btn = Button(window, text='Search Database',command=printtext)
    btn.pack()
    
    btn2 = Button(window, text="Send Mails",command=sendmail)
    btn2.pack()
    
    window.mainloop()