head = 35
leg = 94
r = 0
c = head 
rabbit = 4
chicken = 2
for i in range(35):
    r+=1    
    c-=1
    manyLegs = r*rabbit+c*chicken
    if manyLegs==leg:
        print('Rabbits: ',r,' Chickens: ',c)

'''
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in 
a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
'''