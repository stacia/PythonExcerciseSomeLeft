import collections
word = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split(' ')
word.sort()

countedWord = [[x,count] for x,count in collections.Counter(word).items()]

'''
countedWord = []
for x,count in collections.Counter(word).items():
    countedWord.append([x,count])
'''

for word in countedWord:
    print(word[0],'= ',word[1])

'''for i in range(len(word)):
    for w in word:
        if w 

'''
'''
dupe = [x for x, count in collections.Counter(word).items() if count > 1]
#Same as
dupe = []
for x,count in collections.Counter(word).items():
    if count>1:
        dupe.append([x,count])
print(dupe)
#new_list = [expression(i) for i in old_list if filter(i)]
'''
'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
