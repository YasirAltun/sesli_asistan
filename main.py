import speech_recognition as sr
import time
from datetime import datetime
import webbrowser
import random
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()

def record(ask=False): #sesi  dinlediğimiz fonksiyon
    with sr.Microphone() as source:
       # r.adjust_for_ambient_noise(source, duration=0.01)# ortamdaki  gürlütüye  göre ses tanımlamayı ayarla
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak('anlayamadım!')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice


def response(voice):
    if 'nasılsın' in voice: #nasılsın sorusuna cevap
        speak('iyilik senden')
    if 'saat kaç' in voice: #saat kaç sorusuna cevap
        secenekSaat = ["saat şu an:", "hemen bakıyorum:"]
        secenekSaat = random.choice(secenekSaat)
        saat = datetime.now().strftime('%H:%M:%S')
        speak(secenekSaat + saat)
    if "bugünün tarihi ne" in voice or "hangi tarihteyiz" in voice: #tarih bilgisi sorusu
        tarih = datetime.today().strftime('%d %m %Y')
        speak(tarih)
    if "arama yap" in voice or "ara" in voice or "google da ara" in voice: #google da arama yapabilme
        search = record("ne arayayım")
        url = 'https://www.google.com.tr/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')

    if "angi gündeyiz" in voice or "bugün günlerden ne" in voice or "bugün hangi gün" in voice: #haftanın hangi gününde olunduğu sorusu
        today = time.strftime('%A')
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"
        elif today == "Tuesday":
            today = "Salı"
        elif today == "Wednesday":
            today = "Çarşamba"
        elif today == "Thursday":
            today = "Perşembe"
        elif today == "Friday":
            today = "Cuma"
        elif today == "Saturday":
            today = "Cumartesi"
        elif today == "Sunday":
            today = "Pazar"
        speak("bugün günlerden" + today)

    if 'gidebilirsin' in voice: #kapatma komutu
        speak('görüşürüz')
        exit()




def speak(string):#seslendirme fonksiyonu
    tts = gTTS(text=string, lang="tr", slow=False)
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

while True: #sürekli dinlemesini sağladığı yer
    playsound("ding.mp3") #sürekli dinleme sağlandığı zaman mikrofonun açıldığını belirten zil sesi
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)

