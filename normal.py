var = 0
var2 = True
while var2:
	var = int(input('Insert digit:'))
	if var <= 0 or var >= 10:
		print('Digit is not valid!')
		print('You must insert digit between 0 and 10')
	else:
		var2 = False
var = var ** 2
print(var)