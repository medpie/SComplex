import random
import pandas as pd
import numpy as np
import Graphs as gs
# Generating a random int data in the range [-200, 200]
def random_data(n):
   # n is a postive int.
   data_x = [random.randint(-200,200) for _ in range(n)]
   data_y = [random.randint(-200,200) for _ in range(n)]
   data_x_y = [[data_x[i],data_y[i]] for i in range(n)]
   return data_x_y
#df = pd.DataFrame({'x-values': data_x, 'y-values': data_y})
#print(df)

#print(data)
#data = [[-98, 194], [84, -21], [-143, 59], [168, 24], [-139, -118], [-180, 111], #[53, -16], [-28, -34], [110, 116], [-188, 169]]
def nodes(n):
   S_Complex = [[_] for _ in range(n)]
   return S_Complex

# Creating simplicial complex for a given radius r:

def SimplexTree(r,n):
  # We need to fix the randomly generated data and save it as "data"
  data = [[-98, 194], [84, -21], [-143, 59], [168, 24], [-139, -118], [-180, 111], [53, -16], [-28, -34], [110, 116], [-188, 169]]
  new_S_Complex = nodes(n)
  for i in range(n-1):
     for j in range(i+1,n):
         if (np.linalg.norm([data[i][0] - data[j][0], data[i][1] - data[j][1]]) <=  r):#and (j not in new_S_Complex[i]):         
            new_S_Complex[i].append(j)
            new_S_Complex[j].append(i)
  return new_S_Complex

  

# Making a birth list:

def Simplex_Birth_Death(n):
   radii = [0]
   for r in range(401):
      x = [set(SimplexTree(r,n)[_]) for _ in range(n)]
      y= [set(SimplexTree(r+1,n)[_]) for _ in range(n)]
      if x != y:
         radii.append(r)
   print('Birth times: ', radii)

# Finding the birth-death sequence of i-th simplex:

def Birth_Death(i,n):
   radii_simplex = [0]
   for r in range(401):
      a = SimplexTree(r,n)[i]
      b = SimplexTree(r+1,n)[i]
      if len(a) < len(b):
         radii_simplex.append(r+1)
   print(f'Birth-Death times for simplex {i}: {radii_simplex}')

print(SimplexTree(100,10), SimplexTree(100,10)[1])

#n = 10
# Graphing the SimplexTree(r):
#gs.graphs(SimplexTree(101))

def dim(Scomplex):
      max_list = [len(Scomplex[_])-1 for _ in range(10)]
      return max(max_list)
def dList(Scomplex):
   dim_list = [len(Scomplex[_])-1 for _ in range(10)]
   return dim_list

# making a dictionary of SimplexTree
def dic(Scomplex):
   a = [set(Scomplex[_]) for _ in range(10)]
   dict = {}
   for _ in range(10):
      dict.update({_+1: a[_]})
   return dict

def no_duplicate(S_Complex):
   # removing duplicates
  unique_Complex = []
  new_S_Complex = [set(S_Complex[_]) for _ in range(10)]
  for item in new_S_Complex:
     if item not in unique_Complex:
        unique_Complex.append(item) 
  return unique_Complex





