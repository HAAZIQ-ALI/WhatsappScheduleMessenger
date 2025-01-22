from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os

# Twilio credentials (store in environment variables for security)
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'AC905f64d5edfaaca98f74fdf87c474c73')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'd808b6a74afc29f990e36ca33987ed39')
client = Client(account_sid, auth_token)


def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"Error occurred while sending the message: {e}")


# Input details
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient number with country code (e.g., +123456789): ')
message_body = input(f'Enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM): ')

try:
    # Parse and calculate the scheduled time
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
    current_datetime = datetime.now()

    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print("The specified time is in the past. Please enter a future date and time.")
    else:
        print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

        # Wait until the specified time
        time.sleep(delay_seconds)

        # Send the message
        send_whatsapp_message(recipient_number, message_body)

except ValueError:
    print("Invalid date or time format. Please enter the date in YYYY-MM-DD and time in HH:MM format.")
