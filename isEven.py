def isEven(number):
	dict1={
	'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
	'6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'null'
	}
	lastdig=(dict1[str(int(number))[-1]])
	if 'e' in lastdig and lastdig!='eight':
		return('ODD')
	else:
		return('EVEN')
