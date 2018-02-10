from sys import exit


#  Victory screen
def victory():
	print "You slap the figure sending the mask he was wearing across the room."
	print "You look up only to find... old mister Winklebottom!"
	print "He was just trying to scare you rascally kids off his property the whole time!"
	print "Manslaughter charges are pending though."
	print "Congrats! you made it through"
	print "Restart? (y/n)"
	
	next == raw_input("> ")
	
	if next == "y":
		dirt_road()
	elif next == "n":
		exit(0)


# the living room "level"
def living_room():
	print "You enter the house into an old decrepit living room, if you can still call it that."
	print "suddenly a ghostly figure appears before you, you can either slap the figure or run away\n"
	print "What would you like to do?"
	
	next = raw_input("> ")
	
	if next == "slap the figure":
		victory()
	elif next == "run away":
		dead("While running away you tripped and your head landed on an exposed nail, RIP")

# The front porch "level"
def front_porch():
	print "You walk towards the house and make it onto the front porch."
	print "This place seems to be deserted, the window seems clear enough to"
	print "peek through, or you could just try to open the door.\n"
	print "What do you do?"
	
	next = raw_input("> ")
	
	if next == "peek through the window":
		dead("A hand slams against the glass when you look through, causing a heart attack")
	elif next == "open the door":
		living_room()

# The mailbox "level"
def mailbox():
	print "Inside the mailbox you find only a letter."
	print "Addressed.. to you?\n"
	print "What do you do?"
	
	next = raw_input("> ")
	
	if next == "open the letter":
		dead("Yeah so there was anthrax in the letter. RIP buddy.")
		
	elif next == "close the mailbox":
		dirt_road()
	else:
		print "\tTRY A DIFFERENT COMMAND"
		return mailbox()
		

# Starting area
def dirt_road():
	print "You wake up laying in the middle of a dirt road."
	print "There's a drive way within a few yards of you with a mailbox at the entrance"
	print "Down the drive way you can see an old house, in a state of heavy disrepair\n"
	print "What do you do?"
	
	next = raw_input("> ")
	
	if next == "open the mailbox":
		mailbox()
	elif next == "walk to the house":
		front_porch()
	else:
		print "\tTRY A DIFFERENT COMMAND"
	return dirt_road()

# Title screen
def start():
	print "--------------------------------------------------------"
	print "\tThe Spooky Adventure"
	print "--------------------------------------------------------"
	print "\tType 'start' and hit ENTER to play"
	
	next = raw_input("> ")
	if next == "start":
		dirt_road()
	
	
		
# Death conditions
def dead(why):
	print why, "The spooky boi gotcha"
	print "Would you like to restart? (y/n)"
	
	next == raw_input("> ")
	
	if next == "y":
		dirt_road()
	elif next == "n":
		exit(0)

# Code to launch the title screen	
start()

