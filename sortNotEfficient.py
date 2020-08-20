import sys
from time import perf_counter 
import threading
import random
t2start = perf_counter()  
def shittySort(num):
	ar = []
	i = 0
	j = 1
	while len(ar) < num:
		ar.append(random.randint(1,1000))
	for i in range(len(ar)):

		for j in range(len(ar)-1):
			if(ar[j] > ar[j+1]):
				ar[j], ar[j+1] = ar[j+1], ar[j]
	print(ar)
if __name__ == "__main__":
	t1 = threading.Thread(target=shittySort, args=(1000,)) 
	t1.start()
