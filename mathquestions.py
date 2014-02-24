# Angus Gardner
import sys, random
print "Welcome to Math Questions.\n"

operators = {
	'*': lambda a, b: a * b,
	'+': lambda a, b: a + b,
	'/': lambda a, b: a / b,
	'-': lambda a, b: a - b
}

def question(oper):
	print "You are doing:", typeQ, "\n"
	numQ = int(raw_input("How many questions do you want to be asked?: "))
	lowQ = int(raw_input("What is the lowest value number you want?: "))
	highQ = int(raw_input("What is the highest value number you want?: "))
	for i in range(numQ):
		n1Q = random.randint(lowQ, highQ)
		n2Q = random.randint(lowQ, highQ)
		nanQ = operators[oper](n1Q, n2Q)
		while True:
			print "What is", n1Q, oper, n2Q, "?:"
			ansQ = float(raw_input(""))
			if ansQ == nanQ:
				print "That's right!", ansQ, "is the right answer."
				again = str(raw_input("Again?: "))
				if again.lower() in ('yes', 'y'):
					question(oper)
				elif again.lower() in ('no', 'n'):
					sys.exit(1)
				else:
					print "Exiting."
					sys.exit(1)
			elif ansQ > nanQ:
				print "Too high."
				continue
			elif ansQ < nanQ:
				print "Too low."
				continue

while True:
	typeQ = str(raw_input("What type of questions do you want to be asked?: (Multiplication, Addition, Subtraction, Division) "))
	if typeQ.lower() == 'multiplication':
		question('*')
	elif typeQ.lower() == 'addition':
		question('+')
	elif typeQ.lower() == 'division':
		question('/')
	elif typeQ.lower() == 'subtraction':
		question('-')
	else:
		print "Try again."
		continue
