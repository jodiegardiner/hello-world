
name = raw_input("Enter your name:- ")

print "Hello, " + name.capitalize() + "."

game_decision = raw_input("Would you like to play a game? (y/n)")


if game_decision.capitalize() == "Y":
    print "You die in a horrible global thermonuclear war!  Oops."

else:
        print "Good choice, the only way to win is not to play"