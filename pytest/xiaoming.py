h=float(input('high: (cm)'))
w=float(input('wight:(kg)'))
bmi=w/h/h
tag=['轻量','正常','过重','肥胖','严重']
if bmi < 18.5 :
	print(tag[0])
elif bmi < 25 :
	print(tag[1])
elif bmi < 28 :
	print(tag[2])
elif bmi <32 :
	print(tag[3])
else :
	print(tag[4])
