n=int(input())
words=[]
for i in range(n):
    words.append(input())
newWords=list(set(words))
newWords.sort(key=lambda x: (len(x), x))

for i in range(len(newWords)):
    print(newWords[i])