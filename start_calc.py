import calc

def prompt():
	try:
		while True:
			request = raw_input("Enter 2 numbers and operation (like 2+2.4 or 1/5).\nAvailable: +,-,*,/\nOr enter one integer and operation \"!\"(like 5!)\nCtrl+D to quit\n")
			print calc.calculate(request)		
	except Exception:
		print "Bye!"

if __name__ == "__main__":
	prompt()