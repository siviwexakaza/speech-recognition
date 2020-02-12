import speech_recognition as speech

recognizer = speech.Recognizer()
with speech.Microphone() as mic:
    print('Speak')
    sound = recognizer.listen(mic)
    mic_data = recognizer.recognize_google(sound)
    print(mic_data)
    