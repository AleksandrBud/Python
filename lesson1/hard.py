name = input('Isert your name:')
second_name = input('Insert you second name:')
age = int(input('Insert your age:'))
weight = float(input('Insert your weight:'))
result = name + ' ' + second_name + ', ' + str(age) + ' years, weight ' + str(weight) + ' - '
if age <= 30 and weight >= 50 and weight <= 120:
	result = result + 'хорошее состояние.'
elif age > 30 and (weight < 50 or weight > 120):
	if age > 40 and (weight < 50 or weight > 120):
		result = result + 'следует обратиться к врачу.'
	else:
		result = result + 'следует заняться собой.'
else:
	result = result + 'требуется дополнительное обследование.'
print(result)