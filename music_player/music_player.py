from playsound import playsound

songName = input("Enter song name: ")

while True:
    if songName == "stay":
        print("playing stay by the kid laroi and justin beiber...")
        playsound('stay.mp3')
        break
    
    #elif songName == "let me down slowly":
     #   print("playing let me down slowly by alec benjamin...")
      #  playsound('letmedownslowly.mp3')
       # break