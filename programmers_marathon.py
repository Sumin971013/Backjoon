def letter_count(word):
    counter={}

    for i in word:
        if i not in counter:
            counter[i]=0

        counter[i]+=1

    return counter  


a="hello word"

print(letter_count(a))