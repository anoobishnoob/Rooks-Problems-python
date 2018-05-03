import math
import random
print("We are going to see the probablity of two rooks being in killing range of each other. \nType in how many rounds you would like to play.")
success = 0 
i = 0 
n = int(input())
while (i < n ):
  row1 = math.floor(8*random.random()) # rook 1
  col1 = math.floor(8*random.random())
  
  row2 = math.floor(8*random.random()) # rook 2
  col2 = math.floor(8*random.random())
  
  while (row1 == row2 and col1 == col2):
    row1 = math.floor(8*random.random()) #cathes my rook 1/2 problem 
    col1 = math.floor(8*random.random()) # landing on the same space
  if(row1 == row2 or col1 == col2):
    success +=1 
  i+=1
  
print (success/n)
