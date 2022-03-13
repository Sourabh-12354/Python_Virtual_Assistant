import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import wikipedia
import os
import smtplib
global human
global machine
human = 'You: '
machine = 'Pori: '
listener = sr.Recognizer() ##for  voice recognization
engine = pyttsx3.init() #for text to speech
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
def my_assistant():
    name='Hello I am Pori'
    engine.say(name)
    print(machine+name)
    work='What Can I do for you?'
    engine.say(work)
    print(machine+work)
    engine.runAndWait()

def my_assistant2(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as Source:
            print("Listening.......")
            voice = listener.listen(Source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pori' in command:
                print(human+command)
                my_assistant()
            else:
                print(human+command)
    except:
        pass
    return command
def run_assistant():
    cmnd=take_command()
    if 'play' in cmnd:
            song=cmnd.replace('play','')
            my_assistant2('playing'+song)
            print(machine+'playing'+song)
            kt.playonyt(song)
    elif 'developed' in cmnd:
        dev='Souhardo Sourabh has Developed Me'
        my_assistant2(dev)
        print(machine+dev)
    elif 'time' in cmnd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        var= "It's "
        print(machine+var +time+' O clock')
        my_assistant2(var+time+ ' O clock')
    elif 'who is' in cmnd:
        person = cmnd.replace("who is",'')
        info = wikipedia.summary(person,2)
        print(machine+info)
        my_assistant2(info)
    elif 'are you in relationship' in cmnd:
        ans="Yes,I am in relationship with Souhardo"
        print(machine+ans)
        my_assistant2(ans)
    elif 'whatsapp' in cmnd:
        time = datetime.datetime.now().strftime('%H:%M')
        hours, minutes = time.split(":")
        converted_hours=int(hours)
        convert_minutes=int(minutes)+2
        msg=cmnd.replace("whatsapp"," ")
        wait_req=f"sending message {msg}.Please wait!!"
        print(machine+wait_req)
        my_assistant2(wait_req)
        kt.sendwhatmsg("++8801779862189",msg,converted_hours,convert_minutes)
    elif 'google' in cmnd:
        src=cmnd.replace("google"," ")
        print(machine+'Searching..'+src)
        my_assistant2('searching'+src)
        kt.search(src)
    elif 'shutdown' in cmnd:
        sec=10
        os.system(f"shutdown /s /t {sec}")
        voice=f"Ok!!I am shutting down your pc within {sec} seconds"
        my_assistant2(voice)
        print(machine+voice)
    elif 'mail' in cmnd:
        rplc=cmnd.replace('mail','')
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('roybiswes@gmail.com','SBshowrav12345')
        send="Ok!!Sending Mail."
        print(machine+send)
        my_assistant2(send)
        server.sendmail('roybiswes@gmail.com',
                        'sbshowrav@gmail.com',
                        rplc)
    elif 'wish me' in cmnd:
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            print(machine+'Good Morning.')
            my_assistant2('Good Morning.')
        elif hour>=12 and hour<18:
            print(machine+'Good Afternoon.')
            my_assistant2('Good Afternoon.')
        else:
            print(machine+'Good Evening.')
            my_assistant2('Good Evening.')
    elif 'virtual studio' in cmnd:
        path="C:\\Users\\SOUHARDO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        print(machine+'Opening Virtual Studio.')
        my_assistant2('Opening Virtual Studio')
        os.startfile(path)
    elif 'browser' in cmnd:
        path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        print(machine+'Opening Chrome Browser.')
        my_assistant2('Opening Chrome Browser')
        os.startfile(path)
    elif 'code block' in cmnd:
        path="C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
        print(machine+'Opening Codeblocks.')
        my_assistant2('Opening Codeblocks')
        os.startfile(path)
    elif 'android studio' in cmnd:
        path="C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
        print(machine+'Opening Android Studio.')
        my_assistant2('Opening Android Studio')
        os.startfile(path)
run_assistant()
