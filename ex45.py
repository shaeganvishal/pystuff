'''
Want to create a game that is a text - prompt based game
that will firstly take your name - deliver a personalised message then begin the game
game will be extremely simple
will be a modification on ex38 of lpthw

game will start in a corridor/starting area and proceed to describe scenario

akin to getting a pot of gold at the end of the rainbow

between you and the end gold(geddit) are 3 rooms
Each room will have different functions
1 room will be the death room - you go in and die, Simple - regardless of action
1 room will be the riddle room - must solve simple riddle - might customise riddle based on player?
1 room will be the loop room - you go in, think youre doing soemthing and loop back to the starting area - a message will inform you what a muppet you are

Death Room -
    you enter and are faced with a bear sitting in front of a door
    the bear sees you and you see it
    youre given a prompt to choose 2 things
        dodge or roll - neither are good enough - you die
    call function play again? or not

Riddle Room -
    you enter the room and see a straight path to the door ahead
    a wild gandalf appears and ask you a riddle
    if solved - proceed to win
    if not - he hits you on the head and bellows 'YOU SHALL NOT PASS' - loop to ensure riddle is solved
    game ends

Loop Room -
    enter room
    see a door with no obstruction -
    sends you back to starting area
    message tells you youre a muppet
    try again asshole

after win
show message of what you've won
make message snarky

end
'''
from sys import exit
#should this be its own function?
def welcome_message():
    print "Welcome to Adventure Land! What lies before will be the single greatest most awesome adventure of your life!" + line_break + "maybe.\n\nFirst, your name; first and last if you will."
    return

def personalised_player_message():
    player_name = raw_input("> ")
    print " "
    print player_name
    if "Jeremy" in player_name:
        print "Be careful of old friends who ask you to check out their 'Projects'.\nYes, fuck you too.\nAlright, let's start."
    elif "Peter" in player_name:
        print "Enough rockets for launch(get it?), you're going on an adventure!(Get it, again?).\nAlright, no more sitting around doing nothing, let us begin."
    elif "Sarah" in player_name:
        print "This code may not be great, but I know you are grateful. \nSuch powerful words. Ok let's start."
    else:
        print "Who are you? Fuck off!\nGame over comrade."
        exit(0)
    return

def opening_scrawl():
    print "\t\tADVENTURE LAND \n\t\tEPISODE I"
    print "\tAfter a devasting shipwreck and violent storm, \n\tOur weary traveller, %r, is washed ashore upon \n\tand island unseen by humanity since that green \n\tguy once appeared as a spooky ghost to a kid." % player_name
    print "\tAs %r regains their senses, a light in the distance signals hope. \n\tThat maybe, there is a way back to civilisation. \n\tAfter trekking the harsh jungles, and contracting a fatal dose of malaria," % player_name
    print "\t%r arrives at the entrance to a large temple." % player_name
    print "\tOur hero, unwavering and probably already dying, enters. \n\tWhat treasures they'll find, who knows....."
    print line_break
    temple_entrance()
    return

def temple_entrance():
    print "You enter the temple and in unison the torches alight on the corridor,..........weird.\nYou are presented with a simple option.\nChoose a door, of which there are 3."
    print "A large engraving above them all reads: \n\tHere you see, doors of three,\n\tPick among them, so you may flee.\n\tOne shall take your life, one shall drive you mad, \n\tBut one among them, shall line your pockets and make you glad."
    print " "
    print "With your options presented, numbers alight on the doors in unison.......again, weird.\nThe choices \n\t\t1\t\t\t2\t\t\t\t3"
    player_choice_door()
    return

def player_choice_door():
    door = raw_input("> ")
    message = " What wonders lie behind it, we shall soon see."
    if door == "1":
        print "The ground rumbles as you turn toward the left and proceed through Door 1." + message
        door_one()
    elif door == "2":
        print "The ground rumbles as you proceed dead ahead toward Door 2." + message
        door_two()
    elif door == "3":
        print "The ground rumbles as you turn right and proceed through Door 3." + message
        door_three()
    else:
        print "Hey asshole, keep it between 1 to 3. Let's try again shall we."
        player_choice_door()
    return

def door_one(): #death room
    print line_break
    print "You enter the room and behold the wonders it offers.\nIn this case, a bear. The same one from The Revenant, sitting in front of a door at the end of the room."
    print "You have a few choices to defeat this bear:"
    print "\t1. Dodge around it as it strikes. \n\t2. Roll underneath it as it strikes. \n\t3. Play dead and inch past it like a worm."

    choice = raw_input("> ")
    unseccussful_message = "You were unsuccessful.\nThe bear strikes your face off.\nYou're dead dumbo.\nGame Over!"
    if choice == "1":
        print unseccussful_message
        exit(0)
    elif choice == "2":
        print unseccussful_message
        exit(0)
    elif choice == "3":
        print "That was the stupidest fucking move ever.\nThe bear eats you alive and you die a slow painful death.\nSAD!\nGame Over!"
        exit(0)
    else:
        print "DOES NOT COMPUTE!\nYou're Dead!\nGame Over!"
    return

def door_two(): #riddle room
    riddle_message = "Here's your riddle:"
    riddle_fail_message = "'Fool of a Took!'\n'YOU SHALL NOT PASS!'\nYou die and the game ends!"
    print line_break
    print "A bright light shines in fron of you.\nThe White Wizard approaches........Gandalf, it's Gandalf.\nHe looks up towards you, and bellows; \n'You dare thread into this sacred land? Very well then. Solve this riddle and you shall pass."

    if "Jeremy" in player_name:
        print riddle_message
        print "Two plus two is four, minus one that's...."
        answer = raw_input("> ")
        if "three" in answer or "3" in answer:
            print "QUICK MATHS!\nYou have passed! Proceed to glory."
            winning_room()
        else:
            print riddle_fail_message
            exit(0)
    elif "Peter" in player_name:
        print riddle_message
        print "You can see me in water, but I never get wet. What am I?"
        answer = raw_input("> ")
        if "reflection" in answer:
            print "Yes! Brilliantly done if I do say so myself.\nAlright then, off you go to claim your prize."
            winning_room()
        else:
            print riddle_fail_message
            exit(0)
    elif "Sarah" in player_name:
        print riddle_message
        print "The bubble in your tea, announces Imperial arrival. Name the tea."
        answer = raw_input("> ")
        if "Gong Cha" in answer or "gong cha" in answer or "gongcha" in answer:
            print "China bows before you. \nYou may pass."
            winning_room()
        else:
            print riddle_fail_message
            exit(0)
    else:
        print "If you see this, something went wrong and I don't know what it is. Game Over is guess!"
        exit(0)
    return

def door_three(): #loop back to corridor
    print line_break
    print "Huh? An empty, two doors and a sign saying 'Just pick one, no stress.'\n Ok, abit weird, but alright.\nWhich door would you like?\n\t1\t\tor\t\t\t2?"
    answer = raw_input("> ")
    for answer in answer:
        print "You proceed through the door, and creep through the small passageway. You begin to see a light, freedom!\nWait....."
        temple_entrance()
    return

def winning_room():
    print line_break
    print "Congratulations! You've won the game!\nYour prize is a cool Million Doubloons!\nThe doors being you are shut though, and there doesnt seem to be a passageway out.\nYou die living the dream, being rich.\nGoodbye."
    exit(0)
    return

def start_game(): #function that runs whole game start to finish
    welcome_message()
    personalised_player_message()
    print line_break
    opening_scrawl()
    print line_break
    temple_entrance

#global variables below
line_break = "\n" * 5
player_name = raw_input("> ") #why does door_two not recognise player name from from a different function? when player name is defined " " globally and then specifically in fucntion personalised_player_message?

#Game starts below
start_game()
