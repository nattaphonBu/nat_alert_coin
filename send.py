import smtplib
fromaddr = 'me_email'
toaddrs  = 'you_email'
msg = "\r\n".join([
"From: me_email",
"To: you_email",
"Subject: Just a message",
"",
"Why, oh why"
])
username = fromaddr
password = 'app_password'
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
