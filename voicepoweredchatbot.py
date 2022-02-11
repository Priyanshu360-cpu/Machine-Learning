
  
import speech_recognition as sr
import pyttsx3 
import requests
import json


r = sr.Recognizer() 
  

def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
      
while(1):    
      

    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
  
            print("Did you say "+MyText)
            response = requests.get("https://api.affiliateplus.xyz/api/chatbot?message="+MyText+"&botname=Techie&ownername=Priyanshu")
            data = response.text
            parse_json = json.loads(data)
            SpeakText(parse_json["message"])
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")