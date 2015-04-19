for i in range(1,10):
	print("  "*8*(i-1),end='')
	for j in range(i,10):
		if((i*j)<10):print(i,'*',j,'=',i*j,"      ",end='')
		else:print(i,'*',j,'=',i*j,"     ",end='')
	print(end='\n')
input()