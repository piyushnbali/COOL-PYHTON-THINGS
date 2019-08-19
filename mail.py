import smtplib

def sendemail():
    GMAIL_USERNAME = "sdgfsegwe@email.com"  # your mail
    GMAIL_PASSWORD = "xvsvsvsrrgr00@" # your password goes here

    recipient = "saish3147@gmail.com"     #client mail
    body_of_email = "Hi i liked your profile and interseted to catch up with you "
    email_subject = "It's a match from tinder"

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    # message to be sent
    headers = "\r\n".join(["from: " + GMAIL_USERNAME,
                           "subject: " + email_subject,
                           "to: " + recipient,
                           "mime-version: 1.0",
                           "content-type: text/html"])

    content = headers + "\r\n\r\n" + body_of_email
    s.sendmail(GMAIL_USERNAME, recipient, content)
    s.quit()

for i in range(100):

 sendemail()
