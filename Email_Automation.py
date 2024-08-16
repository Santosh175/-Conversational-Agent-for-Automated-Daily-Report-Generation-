import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(report_file, recipient_email):
    # Your email sending code here
    # Set up email credentials
    sender_email = 'sender_mail@gmail.com'
    app_password = 'sender_mail_account _app _password'

    # Define the email body
    email_body = """Dear Team, Please find the daily sales report attached. Best regards, [Your Name]"""

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'Daily Sales Report'

    # Attach the email body
    msg.attach(MIMEText(email_body, 'plain'))

    # Attach the report
    with open(report_file, 'rb') as f:
        part = MIMEApplication(f.read(), Name='todays_sales_report.pdf')
        part['Content-Disposition'] = 'attachment; filename="todays_sales_report.pdf"'
        msg.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to send email: {e}")

def schedule_email(recipient_email, schedule_time):
    schedule.every().day.at(schedule_time).do(send_email, 'todays_sales_report.pdf', recipient_email)
    while True:
        schedule.run_pending()
        break  # Exit the loop after sending the email

# Test
'''recipient_email = 'recipient@example.com'
schedule_time = '08:00'  # Schedule the email to be sent at 8:00 AM
schedule_email(recipient_email, schedule_time)'''
