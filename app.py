import speech_recognition as speech

recognizer = speech.Recognizer()

def listen():

    with speech.Microphone() as mic:
        
        sound = recognizer.listen(mic)
        words =''
        try:
            words = recognizer.recognize_google(sound)
            
        except speech.UnknownValueError:
            print('Can not understand that...')
        except speech.RequestError:
            print('Please check your internet connection...')
        return words

def command(cmd):
    if 'what is your name' in cmd:
        print('My name is Bella')


print('Voice recognizer started, say something...')
results = listen()
command(results)
