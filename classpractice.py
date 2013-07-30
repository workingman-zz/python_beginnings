""" if we are in mars or earth, we can go to death, or the other planet
	if we get the answer to the question correct. You die and exit if you
	get in wrong.

"""

from sys import exit

class Engine(object):
	
	def __init__(self, start_planet):
		self.start_planet = start_planet

	def play(self):
		if self.start_planet == 'Earth':
			earth.enter()
		elif self.start_planet == 'Mars':
			mars.enter()
		else:
			print "ERROR"
		exit(1)

	def next_planet(self, answer):
		if answer == 'Earth':
			earth.enter()
		elif answer == 'Mars':
			mars.enter()


class Death(object):
	
	def end(self):
		print "The game has ended because you are dead."


class Earth(object):
	
	def enter(self):
		print "You are now on earth."
		print "Monkeys are mammals, True or False?"
		x = raw_input(">  ")
		if x == "True":
			engine.next_planet('Mars')	# get the answer correct
		elif x == "False":
			death.end()

class Mars(object):

	def enter(self):
		print "You are now on Mars."
		print "Whales are fish, True or False?"
		x = raw_input(">  ")
		if x == "True":
			death.end()
		elif x == "False":
			engine.next_planet('Earth')


# create instances of Earth and Mars and Engine.

earth = Earth()
mars = Mars()
death = Death()
engine = Engine("Mars")
engine.play()





