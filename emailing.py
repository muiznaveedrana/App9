import smtplib
from email.message import EmailMessage
import imghdr
sender = "littlecoders10@gmail.com"
password = "byzf java eptn qokk"
reciever = "muiznaveedrana@gmail.com"
def send_email(image_path):
    print("send email function start")
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected VIA Webcam"
    email_message.set_content("Make sure this is safe!")
    
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype = "image", subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, reciever, email_message.as_string())
    gmail.quit()
    print("send email function ended")

if __name__ == "__main__":
    send_email()