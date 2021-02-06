# Coding utf-8

import tkinter as tk
from tkinter import ttk
import smtplib, ssl
from tkinter import messagebox
from tkinter.constants import ANCHOR, CENTER

window = tk.Tk()

# EMAIL CONFIGURATION
smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'example@example.com' # Your GOOGLE ACCOUNT HERE!
password = 'password' # Your password GOOGLE ACCOUNT HERE!

def send_email(entry1, entry2, body):
    receiver = entry1.get()
    subject = entry2.get()
    text = body.get("1.0", "end-1c") 

    if len(receiver and subject and text) == 0:
        messagebox.showwarning(title = 'Error', message= 'Complete all the fields.')
    else:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            message = 'Subject: {}\n\n{}'.format(subject, text)
            server.sendmail(sender_email, receiver, message)
            messagebox.showinfo(title = 'Email', message='The email was sent correctly.')
            window.quit()

def main():
    window.title('E-mailer')
    window.geometry('750x530')
    window.rowconfigure(0, minsize = 20)
    window.rowconfigure(1, minsize = 30)
    window.rowconfigure(2, minsize = 40)
    window.rowconfigure(3)
    window.rowconfigure(4, minsize = 50)
    window.columnconfigure([0, 1], minsize= 50)

    label0 = tk.Label(window, text= ' A small promgram to send emails with Python.', justify='center')
    label1 = tk.Label(window, text = 'Send email to: ', anchor = 'e', justify = 'left')
    entry1 = tk.Entry(window, width = 50, borderwidth=0, bg='light yellow')
    label2 = tk.Label(window, text = 'Subject: ', anchor = 'e', justify = 'left')
    entry2= tk.Entry(window, width = 50, borderwidth= 0, bg='light yellow')
    bodyentry = tk.Label(window, text = 'Body: ', anchor = 'e', justify = 'left')
    body = tk.Text(window, bg='light yellow', bd= 1)
    btn = tk.Button(window, command = lambda: send_email(entry1, entry2, body), text = 'Send Email', width = 15)

    label0.grid(row=0, column = 1, sticky= 'n')
    label1.grid(row = 1, column = 0, sticky = 'ew')
    entry1.grid(row = 1,  column = 1, sticky = 'ew')
    label2.grid(row = 2, column = 0, sticky = 'ew')
    entry2.grid(row = 2,  column = 1, sticky = 'ew')
    bodyentry.grid(row = 3, column = 0, sticky = 'ne')
    body.grid(row = 3, column = 1, sticky = 'ew')
    btn.grid(row = 4, column= 1)
    window.mainloop()

if __name__ == '__main__':
    main()

