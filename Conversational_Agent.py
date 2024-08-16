from Data_Extraction import extract_sales_data
from Report_Generation import generate_report
from Email_Automation import send_email, schedule_email

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer

import re


def process_user_input(user_input):
    # Extract recipient email
    recipient_email = None
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    match = re.search(email_pattern, user_input)
    if match:
        recipient_email = match.group()

    # Extract schedule time
    schedule_time = None
    time_pattern = r'\d{1,2}:\d{2}'
    match = re.search(time_pattern, user_input)
    if match:
        schedule_time = match.group()

    # Determine the user's intent
    if 'generate' in user_input and 'report' in user_input:
        return 'generate_report', recipient_email, schedule_time
    elif 'send' in user_input and 'mail' in user_input:
        return 'send_mail', recipient_email, schedule_time
    elif 'schedule' in user_input and 'mail' in user_input:
        return 'schedule_mail', recipient_email, schedule_time
    elif 'exit' in user_input :
        return 'Thanks_note',None, None
    else:
        return 'unknown', None, None

def handle_user_input(user_input):
    intent, recipient_email, schedule_time = process_user_input(user_input)
    if intent == 'generate_report':
        # Generate the report
        sales_data = extract_sales_data('Sample Sales Data- Interns task.xlsx')
        generate_report(sales_data)
        return 'Report generated successfully!'
    
    elif intent == 'send_mail':
        # Send the mail
        if recipient_email:
            send_email("todays_sales_report.pdf", recipient_email)
            return 'mail sent successfully!'
        else:
            print(recipient_email)
            return 'Please specify recipient email.'
    elif intent == 'schedule_mail':
        # Schedule mailing at a time
        if recipient_email and schedule_time:
            schedule_email(recipient_email, schedule_time)
            return 'Email scheduled & sent successfully'
        else:
            return 'Please specify recipient email and schedule time.'
        
    elif intent == 'Thanks_note':
        return 'thanks , See you Soon !!'
    else:
        return 'Sorry, I didn\'t understand your request.'

def main():
    print()
    print('Welcome to the Mailmitra , how I can help you ? ')
    while True:
        print()
        user_input = input('Please enter your request: ')
        response = handle_user_input(user_input)
        print(response)
        if response == 'thanks , See you Soon !!' : # Exit condition
            break

if __name__ == '__main__':
    main()