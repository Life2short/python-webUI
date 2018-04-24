import smtplib
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename
import CommonLibrary.CommonConfiguration as cc
import CommonLibrary.ResultFolder as ResultFolder


def send_email(send_from, send_to, subject, text, files=None, server="smtp.qq.com"):
    # assert(isinstance(send_to,list),"Send To email should be a list")

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    password = "fcvflxcohhcibjba"

    msg.attach(MIMEText(text, 'html'))

    with open(files, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(files))
        msg.attach(part)
    smtp = smtplib.SMTP_SSL(server, 465)
    smtp.set_debuglevel(0)
    smtp.login(send_from, password);
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


def send_report():
    send_f = "296278505@qq.com"
    send_t = "837123073@qq.com"

    subject = "[Automaiton]TestReport_" + str(datetime.today())

    files =ResultFolder.GetRunDirectory() + "\TestResult.html"
    with open(files, 'r') as f:
        text = f.read()

    send_email(send_f, send_t, subject, text, files)