#coding:shift-jis

while True:
	height = raw_input('�g��(m or cm)?:')
	if len(height) == 0:
		break
	if height >= 50:
		height = float(height)
		weight = float(raw_input('�̏d(kg)?:'))
		bmi = weight / (pow(height,2)/10000)
	elif height <= 49:
		height = float(height)
		weight = float(raw_input('�̏d(kg)?:'))
		bmi = weight / pow(height,2)
	
	print('BMI�l��%0.1f�ł��B' % bmi)
	if bmi < 18.5:
		print('�����₹�����ł��B')
	elif 18.5 <= bmi < 25.0:
		print('�W���I�ȑ̌^�ł��B')
	elif 25 <= bmi < 30.0:
		print('���������Ă��܂��B')
	else:
		print('���x�̔얞�ł��B')