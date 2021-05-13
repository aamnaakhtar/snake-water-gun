import random#, playsound
def winning_music():
    """
    Plays the winning music.

    """
    win_music = ["anime wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)
        
def losing_music():
    """
    Plays the losing music.
    
    """
    lose_music = ["Nope.mp3", "Fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print(e)
        
    def tie_music():
        """
        Plays the tie music.
        
        """
        try:
            playsound.playsound("Awkwark Cricket.mp3")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    print("\nWelcome to the Snake Water Gun game!\n\n\n")
    attempts = 1
    your_point = 0
    computer_point = 0
    
    while (attempts<=10):
        lst=["s","w","g"]
        ran=random.choice(lst)
        
        inp = input("Enter your choice \nSnake(s)\t Water(w)\t Gun(g)\n:")
        inp = inp.lower()
        
        if inp=='s' and ran=='s':
            print("\nTie!\n You chose snake and Computer also chose snake.\nNobody gets point.")
           # tie_music()
            
        elif inp=='w' and ran=='w':
            print("\nTie!\n You chose water and Computer also chose water.\nNobody gets point.")
           # tie_music()
            
        elif inp=='g' and ran=='g':
            print("\nTie!\n You chose gun and Computer also chose gun.\nNobody gets point.")
            #tie_music()
            
        elif inp=='s' and ran=='w':
            your_point=your_point+1
            print("\nCONGRATULATIONS! You won this round.\nYou chose snake and Computer chose water.\n The snake drank the water.\n")
            #winning_music()
            
        elif inp=='w' and ran=='s':
            computer_point = computer_point+1
            print("\nOOPS! You lost this round.\nYou chose water and Computer chose snake. \n The snake drank the water.\n")
            #losing_music()
            
        elif inp=='w' and ran=='g':
            your_point=your_point+1
            print("\nCONGRATULATIONS! You won this round.\nYou chose water and Computer chose gun.\n The gun sank into the water.\n")
            #winning_music()
            
        elif inp=='g' and ran=='w':
            computer_point=computer_point+1
            print("\nOOPS! You lost this round.\nYou chose gun and Computer chose water.\n The gun sank into the water.\n")
            #losing_music()
            
        elif inp=='g' and ran=='s':
            your_point=your_point+1
            print("\nCONGRATULATIONS! You won this round.\nYou chose gun and Computer chose snake.\n The gun killed the snake.\n")
           # winning_music()
            
        elif inp=='s' and ran=='g':
            computer_point=computer_point+1
            print("\nOOPS! You lost this round.\nYou chose snake and Computer chose gun.\n The gun killed the snake.\n")
            #losing_music()
            
        else:
            print("Please enter a valid input!\n")
            continue
        
        
        print("\nNo. of guesses left: {}".format(10-attempts))
        attempts=attempts+1
        
        if attempts>10:
            print("\nGame Over!")
            
    print("\nYour score:", your_point," \nComputer's score:" ,computer_point)
    
    if computer_point>your_point:
        print("\nComputer won the game!")
        
    elif your_point>computer_point:
        print("\nCONGRATULATIONS.You won the game!")
        
    else:
        print("\nIt was a tie!")
        print("Invalid")
        
   # print(11-attempts, "No. of guesses left")
   # attempts=attempts+1
    
    #if attempts>10:
     #   print("\nGame Over!\n")
        
            