import collections
word = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split(' ')
word.sort()
countedWord = [[x,count] for x,count in collections.Counter(word).items()]
[print(word[0],'= ',word[1]) for word in countedWord]