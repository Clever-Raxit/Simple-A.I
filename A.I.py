import time


a = "Tom Cruise"

b = "Tom Holland"

time.sleep(2)
print(" ")
que = input("Do you want to answer my question y/n :")

if que == "y":
    print(" ")
    c = input("Do you like Tom Cruise or Tom Holland :")
    print("Let me think.....")
    time.sleep(2)

    if c == a:
        print(" ")
        print("Oh I Got it =>" +" ""Your Mission Is Impossible")
    else:
        print("Your are the spider man")
else:
    time.sleep(2)

    print(" ")
    print("So.....")
    time.sleep(2)
    print(" ")

    print("Ok, Thank you for answering my question lol !")