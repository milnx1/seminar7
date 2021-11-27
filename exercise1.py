try:
	file1=open('brown.txt')
except:
	print('File cannot be opened:', file1)
	exit()
lines=file1.readlines()
file1.close()
dict1={}
file2=open('output.txt','w')
summa=0
for line in lines:
	words=line.split()
	for i in range(len(words)-5):
		key=words[i]+' '+words[i+1]+' '+words[i+2]+' '+words[i+3]+' '+words[i+4]
		if key not in dict1:
			dict1[key]=1
		else:
			dict1[key]+=1

for key in dict1:
	dictionary=key,dict1[key]
	file2.write(str(dictionary))
	file2.write('\n')
	summa+=dict1[key]
average=summa/len(dict1)

print('Average:',average, '   ','Sum:', summa , '   ','Dict length:',len(dict1))
