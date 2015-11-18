import calc

def main_loop():
	try:
		while True:
			request = raw_input("This program can calculate basic binary operations(*/+-) as well as factorial\nExmaples:\n-1+1\n1--2\n5!\nCtrl+D or Ctrl+C to quit\n")
			print calc.calculate(request)		
	except KeyboardInterrupt:
		print "Bye!"
	except EOFError:
		print "See you!"

if __name__ == "__main__":
	main_loop()