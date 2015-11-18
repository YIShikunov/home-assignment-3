import re

ERRMSG = "Please enter a valid request.\n"
matchnum = "(-?\d+(?:\.\d+)?)"
matchposnum = "(\d+)"

def factor(a):
	res = 1
	a = int(a)
	if (a == 0):
		return 1
	for i in range(1, a+1):
		res *= i
	return res

operations = [
(lambda a, b: float(a) + float(b), re.compile('^' + matchnum + "\+" + matchnum + '$')),
(lambda a, b: float(a) - float(b), re.compile('^' + matchnum + "\-" + matchnum + '$')),
(lambda a, b: float(a) * float(b), re.compile('^' + matchnum + "\*" + matchnum + '$')),
(lambda a, b: float(a) / float(b), re.compile('^' + matchnum + "/"  + matchnum + '$')),
(factor, re.compile("^(\d+)!$"))
]

def calculate(request):		
	response = ERRMSG
	try:
		for operation, regexp in operations:
			m = regexp.match(request)		
			if m:
				response = operation(*m.groups())
				break
	except ZeroDivisionError:
		pass
	return response
	