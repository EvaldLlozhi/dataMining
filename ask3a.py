buckets = []

with open("twitter_dataset.txt") as f:
    for line in f:
		parts = line.split("\t")
		try:		
			text = parts[13]
			buck = []
			if not (text.startswith("RT ")):
				words = text.split(" ")
				for word in words:
					if  word.startswith("#") or word.startswith("@"):
						#clear the word
						word = word.replace("#", "")
						word = word.replace("@", "")
						word = word.replace(",", "")
						word = word.replace(".", "")
						word = word.replace("!", "")
						word = word.replace("?", "")
						word = word.replace(":", "")
						word = word.replace("\n", "")
						word = word.lower()
						#
						buck.append(word)
				if len(buck)>0:
					buckets.append(buck)
		except:
			pass


print ("Statistics")

sum = 0
for b in buckets:
	sum = sum + len(b)


items = []
for b in buckets:
	for item in b:
		if not (item in items):
			items.append(item)

f = open('buckets.txt', 'w')
for b in buckets:
	for item in b:
		f.write (item)
		f.write (",")
	f.write ("\n")
f.close() 


hist = [0]*20

for b in buckets:
	l = len(b)
	hist[l] = hist[l] + 1
	

print ("Number of baskets: ", len(buckets))
print ("Average basket length: ", float(sum)/float(len(buckets)))
print ("Number of items (NOT distinct):", sum)
print ("Number of DISTINCT items :", len(items))

for i in range(0, len(hist)):
	print (i," ---> ", hist[i])


#Apriori

#def joinset(itemset, k):
#	l = len(itemset[0])
#	for item1 in itemset:
#		for item2 in itemset:
#			count = 0;
#			for it in item1:
#				if it in item2:
#					count = count + 1
#			if


def joinlist(items, k):
	for item in items:
		item.sort()
	
	L = []

	for item1 in items:
		for item2 in items:
			count = 0
			for i in range (0,k-1):
				if item1[i] == item2[i]:
					count = count +1
			if count == k-1 and item1[k-1]!=item2[k-1]:
				temp = []
				for it in item1:
					temp.append(it)
				temp.append(item2[k-1])
				temp.sort()
				if not (temp in L): 
					L.append(temp)

	return L

minsup = 0.01



C = items
L = []
for item in C:
	count = 0
	for b in buckets:
		if item in b:
			count = count + 1
	if float(count)/float(len(buckets)) > minsup:
		L.append(item)


temp = []
for item in L:
	temp.append([item])

L = temp

k=1

print L
while len(L)>0:
	C = joinlist(L,k)
	L = []
	for item in C:
		count = 0
		for b in buckets:
			flag = 1
			for it in item: # an kathe leksi einai mesa sto basket
				if not (it in b):
					flag = 0
			if flag == 1:
				count = count + 1
		if float(count)/float(len(buckets)) > minsup:
			L.append(item)
	print L
	k = k+1
	



#H = [ ["b","a","c"], ["a","b","d"], ["a","b","e"], ["a","x","y"]   ]



#print A

	
	









