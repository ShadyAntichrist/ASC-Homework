#!/usr/bin/python

import random

enemies = {
 'dragon': 'Do you sneak around the dragon and steal some gold off the floor [1] or attempt to talk to the dragon and ask for directions out of the cave [2].',
 'swordsman': 'Do you sneak around the sleeping warrior [3] or use a knife on the ground to slit his throat [4].',
 'archer': 'Do you attempt to sneakily steal a map from the archer [5] or attempt to kill the archer with a rock on the ground [6].',
 'musketeer': 'Do you sneak around the sleeping gunman [7] or attempt to sprint past him [8].'
 }

arrow_choices = [1, 2, 2]
random.shuffle(arrow_choices)

shooting = [1, 2, 2, 3, 4]
random.shuffle(shooting)
a = 1
b = 0
c = 0

print "You awaken to find yourself on a damp rock floor. Fear within you swells and you imagine a terrifying enemy..."
add_enemy = raw_input("What is this enemy you fear? ")
enemies[add_enemy] = 'With your worst nightmare sleeping in front of you, do you [9] sneak around the edge or [10] pick up one of the weapons on the floor and attempt to kill it.\n'
random_enemy = random.choice(list(enemies.keys()))

chance = "rock-paper-scissors"
chanceR = chance.split("-")
x = 1
y = 0
z = 0

print "A person walks down the hall and when he comes upon you he challenges you to a rock paper scissors duel."
print "He says due to league rules once your eyes meet with a champs you must do battle."

while (x <= 3):
	your_choice = raw_input("Do you throw rock, paper, or scissors: ")
	while (your_choice != 'rock' and your_choice != 'paper' and your_choice != 'scissors'):
		your_choice = raw_input("Please enter rock, paper, or scissors: ")
	random.shuffle(chanceR)
	champ_choice = chanceR.pop()
	if (your_choice == 'rock' and champ_choice == 'rock' or your_choice == 'paper' and champ_choice == 'paper' or your_choice == 'scissors' and champ_choice == 'scissors'):
		print "You throw %s and he throws %s." % (your_choice, champ_choice)
		print "You tie round %d. Score(you-champ): %d-%d" % (x, y, z)
		x += 1
	elif (your_choice == 'rock' and champ_choice == 'scissors' or your_choice == 'paper' and champ_choice == 'rock' or your_choice == 'scissors' and champ_choice == 'paper'):
		print "You throw %s and he throws %s." % (your_choice, champ_choice)
		y += 1
		print "You win round %d. Score(you-champ): %d-%d" % (x, y, z)
		x += 1
	elif (your_choice == 'rock' and champ_choice == 'paper' or your_choice == 'paper' and champ_choice == 'scissors' or your_choice == 'scissors' and champ_choice == 'rock'):
		print "You throw %s and he throws %s." % (your_choice, champ_choice)
		z += 1
		print "You lose round %d. Score(you-champ): %d-%d" % (x, y, z)
		x += 1
if (y > z):
	print "Congratulations you have bested me and earned your space in the list of great duelists."
	yourTitle = raw_input("What would you like your title to be in the records? ")
	f=open("Champions.txt", "a+")
	for i in range(1):
		f.write("\nOriginal Champion: Balrog the Great\n 2nd Champion: Freed the Conquerer\n 3rd Champion: Bastion the Invincible\n 4th Champion: Artoria Pendragon\n 5th Champion: %s" % yourTitle)
		f.close()
	print "You have been added to the great volume, called Champion.txt"
elif (y < z):
	print "You put up a good fight but in the end are no match for me."
	yourTitle = raw_input("What would you like your title to be in the loss record? ")
	f=open("Fallen.txt", "a+")
	for i in range(1):
		f.write("\n1st Fallen: Mr.Meeseeks\n 2nd Fallen: All Might\n 3rd Fallen: Gon Freecss\n 4th Fallen: Alpha Icarus\n 5th Fallen: %s" % yourTitle)
		f.close()
	print "You have been added to the volume of the fallen, AKA Fallen.txt"
elif (y == z):
	print "For me a draw equals a loss, you have proven yourself good sir."
        yourTitle = raw_input("What would you like your title to be in the list of victors? ")
        f=open("Victors.txt", "a+")
        for i in range(1):
                f.write("\n1st Victor: Rick Sanchez\n 2nd Victor: Izuku Midoriya\n 3rd Victor: Dirty Dan\n 4th Victor: Ted Mosby\n 5th Victor: %s" % yourTitle)
                f.close()
	print "You have been added to the tome of victors, AKA Victors.txt" 

print "The man continues on his way and you look around and see the tunnel extend behind and in front of you, enter [1] to go the path in front of you, [2] to go the path behind you."

path1 = int(raw_input("> "))

while (path1 != 1 and path1 != 2 ):
	print "Please enter [1] or [2]."
	path1 = int(raw_input("> "))
if path1 == 1:
	print "Going forwards you enter a large open spaced cavern in the middle is a sleeping %s.\n" % random_enemy
	print enemies[random_enemy]
	path2 = int(input("> "))
	while (random_enemy == 'dragon' and path2 != 1 and path2 != 2 or random_enemy == 'swordsman' and path2 != 3 and path2 != 4 or random_enemy == 'archer' and path2 != 5 and path2 != 6 or random_enemy == 'musketeer' and path2 != 7 and path2 != 8 or random_enemy != 'dragon' and random_enemy != 'swordsman' and random_enemy != 'archer' and random_enemy != 'musketeer' and path2 != 9 and path2 != 10):
        	print "Please one of the numbers used in your scenario for options."
        	path2 = int(input("> "))
	if path2 == 1:
		print "You make it past the dragon with your pilfered gold and come to a 3 way tunnel split."
		print "Do you go left [1], right [2], or center [3]."
		path3 = int(raw_input("> "))
		while (path3 != 1 and path3 != 2 and path3 != 3):
	     		 print "Please enter [1], [2], or [3]."
       			 path3 = int(raw_input("> "))
		if path3 == 1:
			print "Following the left tunnel you see a man ahead guarding a door, he approaches you."
			print "Do you bribe him with the gold you picked up [1] or attempt to fight him [2]."
			path4 = int(raw_input("> "))
	                while (path3 != 1 and path3 != 2):
                        	 print "Please enter [1] or [2]."
                        	 path1 = int(raw_input("> "))
			if path4 == 1:
				print "The guard takes the gold with a glimmer in his eyes and then steps aside."
				print "You go through the door and see sunlight, smiling you head towards home."
				print "Congrats You Lived. Ending 1/20"
			elif path4 == 2:
				print "You attempt tackle the guard but he easily swats you aside. Then he draws a sword and runs you through the chest."
				print "You Have Died. Ending 2/20"
		elif path3 == 2:
			print "Taking the path on the right you come to an open room, inside are 20 guards eating lunch. The closest ones draw there weapons and charge you, easily they end your life."
			print "You Have Died. Ending 3/20"
		elif path3 == 3:
			print "While taking the center path the floor suddenly gives out and you fall to the bottom of a pit where spikes await you."
			print "You Have Died. Ending 4/20"
	elif path2 == 2:
		print "You approach the dragon and he awakens, you then ask if he knows the way out of this cave and the dragon responds by moving slightly to reveal a tunnel underneath him."
		print "You take the path after thanking the dragon and come to an exit that leads to the outside world."
		print "Congrats you escaped. Ending 5/20"
	elif path2 == 3:
		print "You manage to sneak around the warrior and pick up a dagger on the way through."
		path5 = int(raw_input("You come to a series of turns, do you go left[1], right[2], or center[3]? "))
		while (path5 != 1 and path5 != 2 and path5 != 3):
	     		 print "Please enter [1], [2], or [3]."
       			 path5 = int(raw_input("> "))
		if path5 == 1:
			print "Following the left tunnel you see a man ahead guarding a door, he approaches you."
			print "Do you attempt to sneak up on him [1] or charge him at a sprint [2]."
			path6 = int(raw_input("> "))
	                while (path6 != 1 and path6 != 2):
                        	 print "Please enter [1] or [2]."
                        	 path1 = int(raw_input("> "))
			if path6 == 1:
				print "Taking the guard by surpise you easily cut his throat."
				print "You go through the door and see sunlight, smiling you head towards home."
				print "Congrats You Lived. Ending 6/20"
			elif path6 == 2:
				print "You charge forward at the guard who easily hears you, turning around with his sword drawn he parries your attack and beheads you with his next stroke."
				print "You Have Died. Ending 7/20"
		elif path5 == 2:
			print "Taking the path on the right you come to an open room, inside are 20 guards eating lunch. The closest ones draw there weapons and charge you, easily they end your life."
			print "You Have Died. Ending 3/20"
		elif path5 == 3:
			print "While taking the center path the floor suddenly gives out and you fall to the bottom of a pit where spikes await you."
			print "You Have Died. Ending 4/20"
	elif path2 == 4:
		print "While focusing on the enemy in front of you, you manage trip over some items on the ground and fall right onto some caltrops. Your throat is pierced and you slowly bleed out."
		print "You have Died. Ending 8/20"
	elif path2 == 5:
		print "You manage to sneakily steal the map which has an exit marked on it. While following the map you end up falling into a pit of spikes as the ground breaks apart."
		print "You have Died. Ending 9/20"
	elif path2 == 6:
		print "You quietly approach the sleeping archer with a large rock in hand, upon reaching the archer you bring the rock down crushing his skull."
		print "Taking up the bow of the man you killed you leave the cavern and come across three paths."
		path7 = int(raw_input("Do you follow the left path [1], right path [2], center path [3]? "))
		while (path7 != 1 and path7 != 2 and path7 != 3):
	     		 print "Please enter [1], [2], or [3]."
       			 path7 = int(raw_input("> "))
		if path7 == 1:
			print "Following the left tunnel you see a man ahead guarding a door, he approaches you."
			print "Having never fired a bow before you know this shot with the single arrow the archer had is going to be all luck."
			if arrow_choices[0] == 1:
				print "The arrow misses by a large margin, the guard snickers as he stabs you through the chest."
				print "You have Died. Ending 10/20"
			elif arrow_choices[0] == 2:
				print "Your arrow flies as if guided by apollo himself and pierces the guard straight through the heart."
				print "You proceed passed his fallen body and into the outside world, now you begin your long journey home."
				print "Congrats You Escaped. Ending 11/20"
		elif path7 == 2:
			print "Taking the path on the right you come to an open room, inside are 20 guards eating lunch. The closest ones draw there weapons and charge you, easily they end your life."
			print "You Have Died. Ending 3/20"
		elif path7 == 3:
			print "While taking the center path the floor suddenly gives out and you fall to the bottom of a pit where spikes await you."
			print "You Have Died. Ending 4/20"
	elif path2 == 7:
		print "You attempt to sneak past the sleeping gunman, but on the way you feel a stinging in your chest. You look down to see a bullet hole bleeding profusely."
		print "You have Died. Ending 12/20"
	elif path2 == 8:
		print "While sprinting past the gunman you trip on a nearly invisible wire, as you try to get up the gunman manages to shoot you right in the head."
		print "You have Died. Ending 12/20"
	elif path2 == 9:
		print "Halfway to the exit the %s seemingly senses your presence, it charges you and manages to take you by surprise while your scrambling to get up from your crouched position. Easily your life is ended." % random_enemy
		print "You have Died. Ending 13/20"
	elif path2 == 10:
		print "Grabbing a sword off the ground you charge your mortal enemy, locked in heated combat you match blow for blow and manage to finally hit a major artery. It staggers away and falls to the ground, you have won."
		print "With the head of your nemesis in one hand and a map in the other you make it to a door with a guard in front."
		print "Seeing the head in your hand the guard has fear in his eyes and sprints past you. You exit through the door and see the outside world once again."
		print "You have Survived. Ending 14/20"
elif path1 == 2:
	print "Following the path that the man came from you come across a split in the tunnel."
	path10 = int(raw_input("Do you take the left path [1] or the right path [2]? "))
	while (path10 != 1 and path10 != 2):
		path10 = raw_input("Please enter [1] or [2]: ")
	if path10 == 1:
		print "You come to two doors, one with a question mark sign and with a gun sign."
		path11 = int(raw_input("Do you enter the question mark door [1] or the gun door[2]? "))
		while (path11 != 1 and path11 != 2):
                	path11 = raw_input("Please enter [1] or [2]: ")
		if path11 == 1:
			print "You enter the room and a guard stops you, he says if you can answer his question correctly then you may leave this place through the door behind him."
			print "What is the name of cyborg Birdperson in R&M"
			answer1 = raw_input("> ")
			if (answer1 == 'phoenixperson' or answer1 == 'Phoenixperson'):
				print "Correct, you are free to go."
				print "You Made It Out. Ending 15/20"
			elif (answer1 != 'phoenixperson' or answer1 != 'Phoenixperson'):
				print "Wrong, sorry it had to be this way. The guard shoots you in the chest."
				print "You have Died. Ending 16/20"
		if path11 == 2:
			print "You enter a room with a shooting range, a guard walks up to you and tells you that to leave you must pass a shooting challenge."
			print "The challenge is to hit a bullet in the inner or second innermost circles of a target 3 times out of 4."
			while (a <= 4):
				shooting_result = shooting[0]
				random.shuffle(shooting)
				if (shooting_result == 1 and shooting_result == 2):
					b += 1
					print "You hit ring %d.After shot %d, Score(hit-miss): %d-%d" % (shooting_result, a, b, c)
					a += 1
				elif (shooting_result != 1 and shooting_result != 2):
					c += 1
					print "You hit ring %d.After shot %d, Score(hit-miss): %d-%d" % (shooting_result, a, b, c)
					a += 1 
			if (b > c):
				print "You have passed, you're free to exit through the door behind me"
				print "You have Survived. Ending 17/18"
			elif (b <= c):
				print "You have failed, sorry i have to do this. The guard shoots you in the heart."
				print "You have Died. Ending 18/20"

	elif path10 == 2:
		print "Following the path on the right you come to a door with a guard in front."
		print "The guard says if you can answer his question correctly you can leave this place."
		print "The question is: What is the name of Birdperson's soul-bond?"
		answer2 = raw_input("> ")
		if (answer2 == 'Tammy' or answer2 == 'tammy'):
			print "Correct, you may exit through this door and live your life a free man."
			print "You have Survived. Ending 19/20"
		elif (answer2 != 'tammy' and answer2 != 'Tammy'):
			print "Wrong, sorry about this. The guard stabs you in the throat."
			print "You have Died. Ending 20/20"

