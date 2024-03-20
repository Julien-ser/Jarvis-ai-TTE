import speech_recognition as sr
import pyttsx3 
 
# Initialize the recognizer 
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', 1)
    engine.say('<pitch middle="20">'+command+'</pitch>') 
    engine.runAndWait()
     
# Loop infinitely for user to
# speak
def getText():
    MyText = ""
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=1)
            #r.pause_threshold = 1
             
            #listens for the user's input
            #try:
            audio2 = r.listen(source2)#, duration=4)
            #except Exception as e:
             #   print(e)
              #  return MyText
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            #MyText = MyText.lower()

            #splitText = MyText.split()
            '''match splitText[0]:
                case "how":
                    print("You can become a web developer.")

                case "what":
                    print("You can become a Data Scientist")
                
                case "did":    
                    print("You can become a backend developer")
    
                case "is":
                    print("You can become a Blockchain developer")

                case "are":
                    print("You can become a mobile app developer")
                case _:
                    print("Sorry, what was your question?")
 
            print("Did you say ",MyText)
            SpeakText(MyText)'''
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError as e:
        print(e)
        print("unknown error occurred")

    return MyText

'''
while(1):    
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            splitText = MyText.split()

            match splitText[0]:
                case "how":
                    print("You can become a web developer.")

                case "what":
                    print("You can become a Data Scientist")
                
                case "did":    
                    print("You can become a backend developer")
    
                case "is":
                    print("You can become a Blockchain developer")

                case "are":
                    print("You can become a mobile app developer")
                case _:
                    print("Sorry, what was your question?")
 
            print("Did you say ",MyText)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")'''
