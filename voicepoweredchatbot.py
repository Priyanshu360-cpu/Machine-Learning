
  
import speech_recognition as sr
import pyttsx3 
import requests
import json
import os
import webbrowser



r = sr.Recognizer() 
ytkey="Enter google yt key"  

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
        if "play" in MyText:
            response=requests.get("https://www.googleapis.com/youtube/v3/search/?key="+ytkey+"&part=snippet&q="+MyText.replace("play",""))
            data = response.text
            parse_json = json.loads(data)
            webbrowser.open_new_tab("https://www.youtube.com/watch?v="+parse_json["items"][0]["id"]["videoId"])
        elif "whatsapp" in MyText:
            webbrowser.open_new_tab("https://web.whatsapp.com/")
        else:
            response = requests.get("https://api.affiliateplus.xyz/api/chatbot?message="+MyText+"&botname=Techie&ownername=Priyanshu")
            data = response.text
            parse_json = json.loads(data)
            SpeakText(parse_json["message"])
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")