sentence = input("Enter a sentence : ")
sentence = sentence.lower()
word = sentence.split()
word_count = {}
for words in word:
    if words in word_count:
        word_count[words]+=1
    else:
        word_count[words]=1   

for key,value in word_count.items():
    print(key,value)
        