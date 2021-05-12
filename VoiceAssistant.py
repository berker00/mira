# Ses tanıma
import speech_recognition as SpeechRecognition

# Seslendirme
import playsound as PlaySound
from gtts import gTTS
import os
import random

# İşlevsel kodlar için
from time import ctime
import wikipedia

recognizer = SpeechRecognition.Recognizer()


# Ses tanıma fonksiyonu
def recordAudio():
    with SpeechRecognition.Microphone() as source:
        audio = recognizer.listen(source)

        voiceData = ''

        try:
            voiceData = recognizer.recognize_google(audio)
            print(voiceData)
        except SpeechRecognition.UnknownValueError:
            print('Sorry, I could not get that')
        except SpeechRecognition.RequestError:
            print('Sorry, there is a problem with my service.')

        return voiceData


# Seslendirme fonksiyonu
def speak(audioString):
    textToSpeech = gTTS(text=audioString, lang='en')
    r = random.randint(1, 999999999999)
    audioFile = 'audio-' + str(r) + '.mp3'
    textToSpeech.save(audioFile)
    print(audioString)
    PlaySound.playsound(audioFile)
    os.remove(audioFile)


# Uygulamanın vereceği bazı cevaplar
def respond(voiceData):
    # Asistanın ismi
    if 'what is your name' in voiceData:
        speak('My name is Mira.')
    
    # Nasılsın
    if 'how are you' in voiceData:
        speak('Thanks! How about you?')
        
    # Saat
    if 'time' in voiceData:
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours}:{minutes}'
        speak(time)
    
    # Wikipedia araması
    if 'what is' in voiceData:
        search = voiceData.split('is')[-1]
        try:
            subject = wikipedia.search(search)[1]
            speak('Hold on for a second...')
            speak(wikipedia.summary(subject))
        except:
            speak('There is a problem with this subject. Please try anything else.')
    
    # Uygulamadan çıkış
    if 'goodbye' in voiceData:
        exit()

# Uygulamanın çalıştıracağı kod döngüsü
speak('How can I help you?')
while True:
    voiceData = recordAudio()
    respond(voiceData)
