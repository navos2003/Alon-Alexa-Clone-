import asyncio
import datetime
import os
import pyjokes
import pyttsx3
import pywhatkit
import re
import speech_recognition as sr
import random
import sys
from commands import info, news, weather, alarm, calculator, timer, message
from dotenv import load_dotenv

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('\nListening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        sys.exit()
    return command

def run_alon():
    command = take_command()
    print('\nYou:', command)
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'playing {song}')
        pywhatkit.playonyt(song)
    
    elif 'weather' in command:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(weather.get_weatherInfo())
        talk('Here\'s the weather for today and the daily forecast.')
    
    elif 'message' in command:
        print('\nWhat message do you want to send?')
        talk('What message do you want to send?')
        message_content = take_command()
        print('\nYou:', message_content)
        print('\nSending...')
        talk('Sending')
        load_dotenv()
        phone = os.getenv("PHONE_NUMBER")
        message.send_message(phone, message_content)
        talk('Message sent')

    elif re.match(r'set (a|the) timer', command):
        print('\nHow many seconds to do you want to count down from? (Don\'t say "seconds")')
        talk('How many seconds to do you want to count down from? Don\'t say "seconds"')
        timerSet = str(take_command())
        print('\nYou:', timerSet)
        timerSet = int(timerSet)
        print(f'\nTimer set to {timerSet} second(s)')
        talk(f'Timer set to {timerSet} seconds')
        timer.count(timerSet)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%-I:%M %p')
        print(f'\nCurrent time is {time}')
        talk(f'Current time is {time}')
    
    elif 'news' in command:
        news.get_news()
        talk('Here\'s the newsfeed.')
    
    elif re.match(r'(who|what) (is|are)', command):
        given_info = re.sub(r'(who|what) (is|are)', '', command)
        info.get_info(given_info)
        talk(f'Here\'s the information of {given_info}.')
    
    elif 'calculate' in command:
        exp = command.replace('calculate ', '')
        calculator.calculate(exp)
        talk(calculator.text_to_speech(exp))
    
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(f'\n{joke}')
        talk(joke)

    elif 'knock knock' in command:
        print('\nWho\'s there?')
        talk('Who\'s there?')
        guess = take_command()
        print('\nYou:', guess)
        print(f'\n{guess} who?')
        talk(f'{guess} who?')
        response = take_command()
        print('\nYou:', response)
        print(f'\nNice one, {response}. Thanks for playing.')
        talk(f'Nice one, {response}. Thanks for playing.')

    elif re.match(r'guess (a|the) number', command):
        print('\nGuess a number between 1-5.')
        talk('Guess a number between 1 to 5.')
        random_number = random.randint(1, 5)
        guess = take_command()
        print('\nYou:', guess)
        while int(guess) != random_number:
            print('\nNope, try again!')
            talk('Nope, try again!')
            guess = take_command()
            print('\nYou:', guess)
        print(f'\nCongrats! the number I was thinking was {random_number}')
        talk(f'Congrats! the number I was thinking was {random_number}')

    elif 'alarm' in command:
        talk('\nWhat time do you want me to set the alarm to? Say "set alarm to "')
        alarmSet = take_command()
        print('\nYou:', alarmSet)
        alarmSet = alarmSet.replace("set alarm to ","")
        alarmSet = alarmSet.replace(".","")
        alarmSet = alarmSet.upper()
        talk(f'Alarm set to {alarmSet}')
        alarm.alarm_Func(alarmSet)
        
    else:
        print('\nSorry, I don\'t understand what you\'re trying to say.')
        talk('Sorry, I don\'t understand what you\'re trying to say.')

if __name__ == '__main__':
    print('Hi, I\'m Alon, How can I help you?')
    talk('Hi, I\'m Aelawn, How can I help you?')
    while True:
        run_alon()
        user_input = str(input('\nDo you want to continue (y/n)? '))
        if user_input.lower() in ['no', 'n']:
            print('\nOkay, have a good day.')
            talk('Okay, have a good day.')
            break
