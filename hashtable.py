#hashtable with collision handling
def hashing(x):
	return x%10
def insert(table,key,value):
	print table[hashing(key)]
	if(len(table[hashing(key)]) != 0):
		return True
	table[hashing(key)].append(value)
 
table = [[] for x in range(10)]	
collisionCount = 0

if(insert(table, 114, 'dog')):
	collisionCount += 1
if(insert(table, 5, 'cat')):
	collisionCount += 1
print table
if(insert(table, 15, 'donkey')):
	collisionCount += 1
if(insert(table, 15, 'wolf')):
	collisionCount += 1
print table
print collisionCount
