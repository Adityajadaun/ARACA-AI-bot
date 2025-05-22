import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voices[1].id)
def speak(audio):
      engine.say(audio) 
      engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon ")  
    else:
        speak("Good evening ")
    
    speak("HI I am ARACA ,how may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None" 
    return query

     
if __name__=="__main__" :
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak(f"Sir,opening youtube")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak(f"Sir,opening google")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak(f"Sir,opening whatsapp")
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/search/sajna%20ve%20darshan#login")
            speak(f"Sir,opening spotify")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak(f"Sir,opening instagram")
        elif 'team' in query:
            speak(f"Sir,REPRESENTING YOU THE WONDERFULL TEAM OF MISTER ADITYA PRATAP SINGH AS THE TEAM LEADER AND THE WONDERFULL TEAM MEMBERS ARE ADITYA RAJ , CHAKIT SHARMA , RIDHIMA RAI, ANANYA YADAV")
        elif 'How are You'in query:
            speak(f"I am fantastic sir you tell me about you")    
        elif 'i am also fine' in query:
            speak(f"ohh! nice sir")  
        elif 'play songs' in query:
            webbrowser.open("https://www.youtube.com/watch?v=E2d_tCYAli4")
            speak(f"sure sir,playing your favourite artist songs")