import smtplib, ssl, time

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

sender_email = "therevengeofjake@gmail.com"
password = "44EastM!"
receiver_email = "Alex.Ryley.Smith@gmail.com"

message = """\
Subject: How many times I have gotten revenge: {}

You really thought you could win? I've asked to unsubscribe {} time(s)!"""

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() # Can be omitted
    server.starttls() # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    i = 1
    s = 1
    while i < 11:
        print("Sending email: {}".format(i))
        server.sendmail(sender_email, receiver_email, message.format(i, i))
        time.sleep(s)
        i = i + 1

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 