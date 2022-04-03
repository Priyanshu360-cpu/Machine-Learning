import speech_recognition as sr
import pyttsx3 
import requests
import json
import os
import webbrowser
import pyautogui
import mouse
import screen_brightness_control as sbc
import geocoder
from geopy.geocoders import Nominatim
ki = geocoder.ip('me')
print(ki.latlng)
geoLoc = Nominatim(user_agent="GetLoc")
lat=ki.latlng[0]
long=ki.latlng[0]
maina=str(lat)+","+str(long)
locname = geoLoc.reverse(maina)
print(locname.address)
p=0
r = sr.Recognizer() 
ytkey="Yt Key"  
 
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
  
        print(MyText)   
        if "techno" in MyText:
          SpeakText("I am there at your service Sir")
          p=1
          continue
        if p==1:
         p=0
         if "play" in MyText:
            response=requests.get("https://www.googleapis.com/youtube/v3/search/?key="+ytkey+"&part=snippet&q="+MyText.replace("play",""))
            data = response.text
            parse_json = json.loads(data)
            webbrowser.open_new_tab("https://www.youtube.com/watch?v="+parse_json["items"][0]["id"]["videoId"])
         elif "whatsapp" in MyText:
            webbrowser.open_new_tab("https://web.whatsapp.com/")
         elif "type" in MyText:
             pyautogui.write(MyText.replace("type",""), interval = 0.2)
         elif "power" in MyText: 
             if "lenovo" in MyText:
                 os.system('shutdown /s /t 0')
             else:
                 SpeakText("Wrong Password")
         elif "scroll down" in MyText:
             mouse.wheel(-1)
         elif "left click" in MyText:
             mouse.click('left')
         elif "right click" in MyText:
             mouse.click('right')
         elif "scroll up" in MyText:
             mouse.wheel(1)
         elif "dim light" in MyText:
             sbc.set_brightness(70)
         elif "increase light" in MyText:
             sbc.set_brightness(100)
         elif "say" in MyText:
             SpeakText(MyText.replace("say",""))
         else:
            response = requests.get("https://api.affiliateplus.xyz/api/chatbot?message="+MyText+"&botname=Techie&ownername=Priyanshu")
            data = response.text
            parse_json = json.loads(data)
            SpeakText(parse_json["message"])
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")