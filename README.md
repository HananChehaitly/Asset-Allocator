The purpose of this code is to solve a mathematical challenge that investors encounter when they want to allocate their assets. 

The code outputs the weights that will minimize the variance of a portfolio in order to maximize diversification using **NumPy**. 

The solution is found by using **Lagrange multiplier method** from Calculus, which finds the local maximum and minimum of a multivariate function
subject to a constraint. 

The user needs to enter the number of assets, then the covariances between those assets. 
Investors usually have a ready excel sheet in the following form: 

        1         2          3
      
1     cov(1,1)  cov(1,2)   cov(1,3)


2     cov(2,1)  cov(2,2)   cov(2,3)


3     cov(3,1)  cov(3,2)   cov(3,3)



