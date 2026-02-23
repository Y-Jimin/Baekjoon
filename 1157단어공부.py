counter=[0 for i in range(ord('a'), ord('z')+1)]
word=input()
for i in word:
    if ord(i)<97: #대문자인 경우
        counter[(ord(i)+32)-97]+=1
    else:
        counter[ord(i)-97]+=1
maxcount=max(counter)
if counter.count(maxcount)==1:
    print(chr(counter.index(maxcount)+97-32))
else:
    print('?')