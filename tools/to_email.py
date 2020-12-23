# --*--coding：utf-8 --*--
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from Base.setting import Setting


class SendEmail:
    @staticmethod
    def send_email(filepath):
        # email_to 收件方
        # filepath 发送附件的地址
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = MIMEMultipart()
        msg['Subject'] = Header(now + '接口自动化报告','utf-8')
        msg['From'] = Header('自动化机器人', 'utf-8')
        msg['To'] = Header('熊衍东', 'utf-8')
        # 文字部分
        part = MIMEText('接口自动化报告，请查收', 'plain', 'utf-8')
        msg.attach(part)
        # 附件部分
        part = MIMEApplication(open(filepath, 'rb').read())
        part.add_header('Content-Type', 'application/octet-stream')
        part.add_header('Content-Disposition', 'attachment', filename='接口自动化测试报告.html')
        msg.attach(part)
        s = smtplib.SMTP_SSL(Setting.Email_Host, timeout=30)
        s.login(Setting.From_user, Setting.From_user_pwd)
        s.sendmail(Setting.From_user, Setting.To_user, msg.as_string())
        s.close()



