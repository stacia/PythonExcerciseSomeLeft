'''
Question 21
Level 3

A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

import numpy as np
print('Enter the robot move and followed by its magnitude: (UP, LEFT, RIGHT, DOWN) ')
HORIZONTAL = 0
VERTICAL = 0
while True:
    print('-->',end=' ')
    pos = input().split(' ')
    if pos[0]== 'UP' or pos[0]== 'up':
        VERTICAL+=int(pos[1])
    elif pos[0]== 'DOWN' or pos[0]== 'down':
        VERTICAL-=int(pos[1])
    elif pos[0]== 'RIGHT' or pos[0]== 'right':
        HORIZONTAL+=int(pos[1])
    elif pos[0]== 'LEFT' or pos[0]== 'left':
        HORIZONTAL-=int(pos[1])
    elif pos[0]=='':
        break
    else:
        print('wrong input bro')

distance = (np.sqrt(HORIZONTAL**2+VERTICAL**2))
print('The distance is: ', int(distance))

