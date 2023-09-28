import smtplib, ssl, os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, email, password, host="smtp.gmail.com", port=465):
        self.email = email
        self.password = password
        self.host = host
        self.port = port
        self.context = ssl.create_default_context()

    # Sends Plaint Text Email (No Attachments)
    def plain_mail(self, to, subject, body):
        with smtplib.SMTP_SSL(host=self.host, port=self.port, context=self.context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, to, f"Subject: {subject}\n\n{body}")

    # Sends Email with Attachments
    # Returns True if Successful, else False
    def attachment_mail(self, to, subject, attachment, body=None, mimetype="plain", subtype="csv"):
        if(not os.path.exists(attachment)):
            return False
        
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = self.email
        message["To"] = to
        message["Subject"] = subject

        # Add body to email
        if(body):
            message.attach(MIMEText(body, "plain"))

        filename = attachment
        part = MIMEBase(mimetype, subtype)
        with open(filename, "rb") as attachment:
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        with smtplib.SMTP_SSL(host=self.host, port=self.port, context=self.context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, to, text)
        print("Sent Mail Successfully")
        return True