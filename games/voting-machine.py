print("Welome to the voting machine!")
age = int(input(("Enter you age, so that we can determine if you're allowed to vote: ")))

if age >= 18: 
    
    print("")
    print("You have verified that you are an adult, please continue and vote for the candidate of your choice.")
    
    candidates = [
        '1) Rahul Gandhi', 
        '2) Narendra Modi', 
        '3) Amit Shah', 
        '4) Shashi Tharoor', 
        '5) Pinarayi Vijayan', 
        '6) Suresh Gopi']
    
    print ("")
    print (candidates)
    print ("")
    
    while True:
        
        vote = int(input("Please select the number corresponding to the candidate you would like to vote for. Remember, you have only one vote and you cannot rectify after voting. "))

        if vote == 1:
            print("You have voted for Rahul Gandhi of the Indian National Congress. Thank you for voting!")
            break
        elif vote == 2:
            print("You have voted for Narendra Modi of Bharatiya Janatha Party. Thank you for voting!")
            break
        elif vote == 3:
            print("You have voted for Amit Shah of Bharatiya Janatha Party. Thank you for voting!")
            break
        elif vote == 4:
            print("You have voted for Shashi Tharoor of the Indian National Congress. Thank you for voting!")
            break
        elif vote == 5:
            print("You have voted for Pinarayi Vijayan of Communist Party of India (Marxist). Thank you for voting!")
            break
        elif vote == 6:
            print("You have voted for Suresh Gopi of Bharatiya Janatha Party. Thank you for voting!")
            break
        
        else:
            print("")
            print("Invalid candidate. Please vote for a candidate between number 1 to 6.")
        
else:
    print(f"Sorry, you cannot vote since you are below the age of 18. You will be able to vote in {18-age} years.")