import time
import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty("rate", 120)
print(" ")

hello = print("Hello My Self F.R.I.D.A.Y,")
nice = print("Nice to interact with you!")
ready = print("Are You Ready for banger discussion with F.R.I.D.A.Y y/n")


speaker.say("hello you can call me friday")
speaker.say("it is nice to interact with you")
speaker.say("are you ready for banger discussion with me type y for yes or type n for no")
speaker.runAndWait()

areYouReady = input()


if areYouReady == "y":
    speaker.say("Let us get started")
    speaker.say("there is one requirement")
    speaker.say("Keep your energy high with me.")
    speaker.runAndWait()
    print("let's start our conversations")
    speaker.say("Do you want to answer my question type y for yes or n for no")
    speaker.runAndWait()
    a = "tc"
    b = "th"
    que = input()
    if que == "y":
        speaker.say("so now i will start my questions")
        speaker.say("how can i call you please write your name")
        speaker.runAndWait()
        name = input()
        name_numbers =str(len(name))
        speaker.say("it is nice to meet you" + name)
        speaker.say("your name contains" + name_numbers + "words")
        speaker.runAndWait()
        print("Your name contains "+ name_numbers +" words")
        print("It is nice to meet you "+ name)

        speaker.say("Next Questions")
        speaker.say("Do you like tom cruise or tom holland type t c for tom cruise or type t h for tom holland ")
        speaker.runAndWait()
        c = input()
        if c == a:
            speaker.say("oh man your mission is impossible")
            speaker.runAndWait()
            print("Your Mission Is Impossible")
            time.sleep(2)
            speaker.say("Was that a nice joke")
            speaker.runAndWait()
        else:
            speaker.say("you are a spider man")
            speaker.runAndWait()
            print("Your are the spider man")
            time.sleep(2)
            speaker.say("Was that a nice joke")
            speaker.runAndWait()
    else:
        speaker.say("ok thank you for answering my question ha ha ha")
        speaker.runAndWait()
        print("Ok, Thank you for answering my question lol !")
else:
    speaker.say("at your command sir")
    speaker.say("so i will catch you later")
    speaker.runAndWait()
    print("At your Command Sir! ")
    print("So i will catch you later")
    print()
