import numpy as np
n = int(input('Please enter number of assets: '))

matrix = [[0 for i in range(n+1)] for j in range(n+1)]

for r in range(0,n):
 data = input('Enter first row: ')
 row = list(map(float, data.split(' ')))
 if len(row) == n:
  row = np.array(row)
  row = row*2
  row = np.append(row,-1)
  matrix[r]=row
 else: input('Please enter valid input: ')

matrix[n] =np.append([1 for i in range(1, n+1)],0)
b = [0.0 for i in range(0,n)]
b= np.append(b,1)
print(b)

A= np.array([matrix[r] for r in range(0,n+1)])
print(A)
z =  np.linalg.solve(A,b)
weights = z[0: n]
print('The weights of the portfolio should be: ',weights)
