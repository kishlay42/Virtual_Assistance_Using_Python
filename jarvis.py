import pyttsx3
import speech_recognition as sr 
import datetime 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #choose your voice 
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id) 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<=12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis sir. please give me a command")
def takeCommand():
    # it takes microphone iinout from user and return string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again..")
        return "None"
    return query
def sendEmail(to,content): #Allow less secure app in your google account
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password') #add your gmail and password
    server.sendmail("yoremail@gmail.com",to, content) #add your gmail
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        query= takeCommand().lower()

    #logic to excecute task
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir='C:\\Music' #path where your music is stored
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'email to kishlay' in query:
            try:
                speak("what should I say?")
                content= takeCommand()
                to = "kishlayk7357@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir I was not able to send email!")


 