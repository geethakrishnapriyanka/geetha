import smtplib
FROM="gkpriya1999@gmail.com"
TO="bantudeepthi99@gmail.com"

SUBJECT="mail"
TEXT="hello frnds i learn how to send mail using python"
pwd="Priya@1999"
message="SUBJECT:%s \n\n %s" %(SUBJECT,TEXT)
print(message)
server=smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(FROM,pwd)
server.sendmail(FROM,TO,message)
server.close()
print('successfully sent the mail')
