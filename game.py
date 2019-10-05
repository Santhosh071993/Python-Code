import random
list=['rock','paper','scissor']
user= input('select one of these rock,paper,scissor? : ')
if user in list:
	list.remove(user)
	cmp=random.choice(list)
	print ('Computer Choice :',cmp)
	if user=='rock' and cmp== 'paper':
		print('Paper Win')
	elif user=='rock' and cmp=='scissor':
		print('Rock Win')
	elif user=='paper' and cmp=='scissor':
		print('Scissor win')
else:
	print('You selected Wrong item try agian')