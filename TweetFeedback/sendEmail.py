import smtplib

sender = 'harshit.jaiswal@ukg.com'
receivers = ['harshit.jaiswal@ukg.com']
message = """From: Harshit Jaiswal <harshit.jaiswal@ukg.com>
    To: <harshit.jaiswal@ukg.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: Test Email
    """


def sendEmail(body):
    try:
        smtpObj = smtplib.SMTP('smtp.ukg.com', 25)
        smtpObj.sendmail(sender, receivers, message + body)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
