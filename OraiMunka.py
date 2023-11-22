


def prim1():
	x = int(input("Kérek egy számot: "))
	if x <= 1:
		print("Nem prim")
	elif x == 2:
		print("Prim")
	else:
		oszto_db = 0
		for i in range(3,x-1,1):
			if(x%1==0):
				oszto_db += 1

			if oszto_db == 0:
				print("Prim")
			else:
				print("Nem prim")


#prim1()










def prim2():
	x = int(input("Kérek egy számot: "))
	if x <= 1:
		print("Nem prim")
	elif x == 2:
		print("Prim")
	else:
		oszto_db = 0
		i:int = 2
		while i < x-1 and not (x%i!=0):
			oszto_db += 1
			i += 1

		if oszto_db == 0:
				print("Prim")
		else:
			print("Nem prim")


#prim2()





def Prim3():
	szam = int(input("Kérek egy egész számot: "))
	i = 1
	if szam>2 and szam % 2 == 0 or szam>3 and szam % 3 == 0 or szam>5 and szam % 5 == 0 or szam == 1:
		valasz = f"A {szam} szám nem prím"
	else:
		i = 5
		while i * i <= szam:
			if szam % i == 0 or szam % (i + 2) == 0:
				valasz = f"A {szam} szám nem prím"
				break
			i += 6
		valasz = f"A {szam} szám prím"
	return valasz


#eredmeny3 = Prim3()
#print(eredmeny3)








import random
import math

def veletlen():
	i:int = 0
	while i<5:
		szam = random.random()*(35-10)+10
		i += 1



#veletlen()






def listakiir():
	lista = [2,4,5]
	for i in range(0,len(lista),1):
		print(f"A lista {i}. eleme: {lista[i]}")


listakiir()












