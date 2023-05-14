import random
gg = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
hm = int(input("какая длина?"))
pas = ''
for i in range(hm):
	pas += gg[random.randint(0,len(gg))]
print(pas)
	
	


