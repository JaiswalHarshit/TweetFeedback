import smtplib

sender = 'harshit.jaiswal@ukg.com'
receivers = ['gaurav.mehra@ukg.com','harshit.jaiswal@ukg.com']
message = """From: Harshit Jaiswal <harshit.jaiswal@ukg.com>
    To: <gaurav.mehra@ukg.com>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: Test Email
    """


def sendEmail(body):
    try:
        smtpObj = smtplib.SMTP('smtp.ukg.com', 25)
        msg = 'Subject: {}\n\n{}'.format("Customer Feedback", body)
        smtpObj.sendmail(sender, receivers, msg)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
