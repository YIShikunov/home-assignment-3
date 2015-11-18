import re
from decimal import *

ERROR_MESSAGE = "Please enter a valid expression.\n"
matchfloat = "(-?\d+(?:\.\d+)?)"

def factor(a):
	res = 1
	a = int(a)
	if (a == 0):
		return 1
	for i in range(1, a+1):
		res *= i
	return res

def mult(a, b):
	return str(Decimal(a) * Decimal(b))
	
def divis(a, b):
	try:
		return str(Decimal(a) / Decimal(b))
	except	ZeroDivisionError:
		return ERROR_MESSAGE
def sum(a, b):
	return str(Decimal(a) + Decimal(b))
	
def sub(a, b):
	return str(Decimal(a) - Decimal(b))

operations = {
"+" : sum, 
"-" : sub,
"/" : divis,
"*" : mult}	

def calculate(request):	
	setcontext(BasicContext)
	response = ERROR_MESSAGE
	regexpCalc = re.compile("^" + matchfloat + "([+*\-/]{1})" + matchfloat + "$")
	regexpFactor = re.compile("^(\d+)!$")
	m = regexpCalc.match(request)		
	if m:
		response = operations[m.groups()[1]](m.groups()[0],m.groups()[2])
	else:
		m = regexpFactor.match(request)
		if m:
			response = factor(m.groups()[0])
	return response
	