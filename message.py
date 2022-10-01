import datetime
import pywhatkit

def send_message(phone, message_content):
    pywhatkit.sendwhatmsg(phone, message_content, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
    print('\nMessage Sent!')