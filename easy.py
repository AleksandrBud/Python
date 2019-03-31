#Job 1
var1 = 'text'
var2 = 0
var3 = 0.0
var4 = False
print(var1,var2,var3,var4)

var1 = input('Write what you think about this program:')
print(var1)

#Job2
var2 = float(input('Insert digit:'))
var2 = var2 + 2
print(var2)

#Job3
var3 = int(input('Insert your age:'))
if var3 < 18:
	print('Sorry, you can use it from the age of 18!')
else:
	print('Access is allowed!')