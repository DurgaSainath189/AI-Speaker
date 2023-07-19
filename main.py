import pyttsx3

if __name__ == '__main__':
    print("Welcome to AI Speaker")
    while 1:
        x = input("Enter Your Text: ")
        engine = pyttsx3.init()
        if x == "exit" or x == "bye" or x == "quit":
            engine.say("Thank You Have a Nice Day")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
