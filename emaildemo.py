##import smtplib
##from smtplib import *
##
##sender = 'hariprasaath2002@gmail.com'
##receivers = ['hariprasaath2002@gmail.com']
##
##message = """From: From Person <from@fromdomain.com>
##To: To Person <to@todomain.com>
##Subject: SMTP e-mail test
##
##This is a test e-mail message.
##"""
##
##try:
####   smtpObj = smtplib.SMTP('localhost')
####   smtpObj.sendmail(sender, receivers, message)
####   smptlib.SMTP('smtp.gmail.com',587)
##   session = smptlib.SMTP('smtp.gmail.com',587)
##   session.ehlo()
##   session.starttls()
##   session.ehlo()
##   session.login(sender,'password')
##   session.sendmail(sender,receiver,message)
##   ession.quit()
##   print( "Successfully sent email")
##except SMTPException as a:
##   print ("Error: unable to send email:-",a)

import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = 'hariprasaath2002@gmail.com'
receiver_email = 'jawaharmas@gmail.com'
password = 'hari@2002'
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
