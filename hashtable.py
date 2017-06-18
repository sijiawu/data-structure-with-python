#hashtable with collision handling
def hashing(x):
	return x%10
def insert(table,key,value):
	table[hashing(key)].append(value)
 
table = [[] for x in range(10)]	
 
insert(table, 114, 'dog')
insert(table, 5, 'cat')
print table
insert(table, 15, 'donkey')
print table
