#coding:utf-8
s="12401011801180212011401804"
s=s.split('0')
mids=[[] for i in range(len(s))]
result=[[] for i in range(len(s))]
zuhe=[
    ['1'],
    ['11','2'],
    ['111','21','12','3'],
    ['1111','112','121','211','13','31','4'],
    ['11111','1112','1121','1211','2111','113','131','311','122','212','221','14','41','5']
        ]
print s
for i in range(len(s)):
	num=int(s[i])
	if num<=26:
		mids[i].append(num)
	if len(s[i])==1:
		continue
	num=0
	for j in range(len(s[i])):
		num+=int(s[i][j])
	if num<=26:
		mids[i].append(num)
	if len(s[i])==2:
		continue
	num=0
	if len(s[i])==3:
		num+=int(s[i][0])*10+int(s[i][1])+int(s[i][2])
		if num<=26:
			mids[i].append(num)
		num+=(int(s[i][0])+int(s[i][1]))*10+int(s[i][2])
		if num<=26:
			mids[i].append(num)
print 'mid',mids
for i in range(len(mids)):
	for j in range(len(mids[i])):
		tmpchr=chr(ord('a')+int(mids[i][j])-1)
		result[i].append(tmpchr)
print result

for i in range(len(result)):
	print result[i]
	