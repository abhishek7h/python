from playsound import playsound

songName = input("Enter song name: ")

while True:
    if songName == "heat waves":
        print("playing heat waves by glass animals...")
        playsound("heat_waves.mp3")
        break