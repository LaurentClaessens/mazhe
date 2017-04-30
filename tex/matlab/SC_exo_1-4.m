A = pi*eye(10)
A(1,10) = -1
A(10,1) = 1

inverse = inv(A)
puissance = A^5

diag(inverse)(1:3)
   %0.28903
   %0.31831
   %0.31831


diag(puissance)(1:3)
    %11.665
   %306.020
   %306.020
