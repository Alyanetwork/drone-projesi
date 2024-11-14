# src/modules/sensors/audio_processing.py

import speech_recognition as sr

class AudioProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_for_threats(self):
        with sr.Microphone() as source:
            print("Dinliyor...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language="tr-TR")
                print(f"Saptanan Ses: {text}")
                if "yardım" in text or "tehdit" in text:
                    return "Tehdit tespit edildi!"
                return "Tehdit algılanmadı."
            except sr.UnknownValueError:
                return "Anlaşılamayan ses algılandı."
            except sr.RequestError as e:
                return f"Ses tanıma hatası: {e}"
