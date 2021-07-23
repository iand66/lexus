import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender = 'alver.lesc@gmail.com'
    password = 'nPY9xE8YbEEc-Xa'
    receiver = 'idavies66@gmail.com'
    message = f"""<h3>New Feedback Submission</h3>
            <ul>
                <li>Customer -{customer}</li>
                <li>Dealer -{dealer}</li>
                <li>Rating -{rating}</li>
                <li>Comments -{comments}</li>
            </ul>"""
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

