# HOROSCOPE PROJECT-this can tell future based on your zodiac sign.

print("WELCOME TO ZODIAC WORLD!!!!\n")

nxt=True

while nxt==True:
    print('''
    
    1) ARIES
    2) TAURUS
    3) GEMINI
    4) CANCER
    5) LEO
    6) VIRGO
    7) LIBRA
    8) SCORPIO
    9) SAGITTARIUS
    10) CAPRICORN
    11) AQUARIUS
    12) PISCES
    
    ''')
    
    zod=int(input("Select your zodiac Number and enter it.\n"))
    
    if zod==1:
        print("The beginning of the week is bound to be dominated by questions of money, and what you can and can’t afford will be the overriding issue of the times. Don’t expect everything to be completed today, for there are further changes waiting in the wings.")
    elif zod==2:
        print("A build-up of lively lunar alignments is already sending emotional ripples in your direction. The waters of life may soon be a little choppier than you would like, but you may use any changes in your routine as an opportunity for self-reflection.")
    elif zod==3:
        print("You may be concerned first with how to put your ideas into practice, and secondly with how to prevent certain other people from knowing exactly what you’re planning! Take trusted individuals into your confidence sooner rather than later, and you’ll stand a better chance of getting your way.")
    elif zod==4:
        print("Think ahead. You may be concerned with the need to fulfill immediate responsibilities, but your day will be all the more successful if you have a long-term strategy. This, you see, will enable you to identify the underlying patterns in your affairs.")
    elif zod==5:
        print("The heart of all current questions concerns your ambitious desire to “be somebody”. If you fail to make any effort in this direction you will bring frustration upon yourself. Ultimately, it doesn’t matter whether you succeed or fail, just as long as you try.")
    elif zod==6:
        print("At home and in your private life, you should expect a fair degree of confusion. This is to be welcomed as a sign that change is being forced upon you, giving you the opportunity to make whatever improvements you feel are necessary. Try to ensure that everyone shares in the benefits.")
    elif zod==7:
        print("There is still a great deal to gain from being as generous as possible. Remember all those wise sayings about not living by bread alone, and realise that money is there to be used, not hoarded away. Your high hopes will come to nothing unless you actually get on and do something about them!")
    elif zod==8:
        print("This is a fairly powerful period emotionally, but in many ways less intense than you have come to expect at such moments. The cause celebre of the day could be money, and if you’re wondering just what is going on, give yourself a little more time.")
    elif zod==9:
        print("Get off to an efficient and organised start today. There is no time for early morning blues. Given that there may soon be a brief, stormy period at work, it’s in your interests to be fully prepared. In fact, you'd be advised to steal a march on people at home as well.")
    elif zod==10:
        print("It may be an overstatement to say that this is a moment for unrestrained pleasure, but it is certainly a fine time to give the highest priority to your personal creativity and desire for self-expression. And don’t let someone dent your enthusiasm, however hard they try.")
    elif zod==11:
        print("Get back to basics today. For some of you, this could mean that home and family affairs take up so much time that you never actually get going on anything else. At work, try as best you can to create a cosy atmosphere. Make sure that colleagues know they can rely on you.")
    elif zod==12:
        print("You are very certain of your plans, but less sure about which of them should take priority! It is strange indeed how you can at once be so sure of the future, yet so typically undecided! A useful start would be to check out what you can actually afford.")
    else:
        print("Ooops!!! You entered wrong zodiac Number.\nTry again!!!\n")
        
    nxt=True if input("\nDo you want to continue the game? Enter (Y/N)\n")=="Y" else False
    
print("\nThank you.Hope you have fun!!!\n")
