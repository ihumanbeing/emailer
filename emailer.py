'''by @anactualhuman_
Just send emails i guess
change the email_sender and pwrd to your own and make sure your google account's unsafe app setting is on
and that's basically it
'''

from tkinter import *
import smtplib

root = Tk()
root.title("Emailer")
root.resizable(0,0)
root.iconbitmap('icon.ico')

email_sender = '[your email goes here]'
sender_pwrd = '[your password goes here]'

def send_mail():
    global subject, body
    sub = subject.get("1.0","end")
    bod = body.get("1.0","end")
    person = to.get("1.0","end")
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(email_sender, sender_pwrd)

    msg = f"Subject: {sub}\n\n{bod}"

    try:
        server.sendmail(
            email_sender,
            person,
            msg

        )
        print('Email sent')

        server.quit()
        
    except:
        print('Bitch that aint it')
        
    

txtto = Label(root, text="To: ").grid()

to = Text(root, height=1, width=15, font=("Arial", 12))
to.grid()

txtsubject = Label(root, text="Subject: ").grid()

subject = Text(root, height=1, width=15, font=("Arial", 12))
subject.grid()

txtbody = Label(root, text="Body: ").grid()

body = Text(root, width=40, height=10, font=("Arial", 12))
body.grid()

send = Button(root, bd=0.5, text="Send", command=send_mail).grid()


root.mainloop()
