# 2010 AMC 10B Problem 13

## Problem

What is the sum of all the solutions of $x = \left|2x-|60-2x|\right|$ ?

$\textbf{(A)}\ 32 \qquad \textbf{(B)}\ 60 \qquad \textbf{(C)}\ 92 \qquad \textbf{(D)}\ 120 \qquad \textbf{(E)}\ 124$

## Solution 1
We evaluate this in cases:
Case 1 $x<30$
When $x<30$ we are going to have $60-2x>0$ . When $x>0$ we are going to have $|x|>0\implies x>0$ and when $-x>0$ we are going to have $|x|>0\implies -x>0$ . Therefore we have $x=|2x-(60-2x)|$ . $x=|2x-60+2x|\implies x=|4x-60|$
Subcase 1 $30>x>15$
When $30>x>15$ we are going to have $4x-60>0$ . When this happens, we can express $|4x-60|$ as $4x-60$ . Therefore we get $x=4x-60\implies -3x=-60\implies x=20$ . We check if $x=20$ is in the domain of the numbers that we put into this subcase, and it is, since $30>20>15$ . Therefore $20$ is one possible solution.
Subcase 2 $x<15$
When $x<15$ we are going to have $4x-60<0$ , therefore $|4x-60|$ can be expressed in the form $60-4x$ . We have the equation $x=60-4x\implies 5x=60\implies x=12$ . Since $12$ is less than $15$ , $12$ is another possible solution. $x=|2x-|60-2x||$
Case 2 : $x>30$
When $x>30$ , $60-2x<0$ . When $x<0$ we can express this in the form $-x$ . Therefore we have $-(60-2x)=2x-60$ . This makes sure that this is positive, since we just took the negative of a negative to get a positive. Therefore we have $x=|2x-(2x-60)|$
$x=|2x-2x+60|$
$x=|60|$
$x=60$
We have now evaluated all the cases, and found the solution to be $\{60,12,20\}$ which have a sum of $\boxed{\textbf{(C)}\ 92}$

## Solution 2
From the equation $x = \left|2x-|60-2x|\right|$ , we have $x = 2x-|60-2x|$ , or $-x = 2x-|60-2x|$ . Therefore, $x=|60-2x|$ , or $3x=|60-2x|$ . From here we have four possible cases:
1. $x=60-2x$ ; this simplifies to $3x=60$ , so $x=20$ .
2. $-x=60-2x$ ; this simplifies to $x=60$ .
3. $3x=60-2x$ ; this simplifies to $5x=60$ , so $x=12$ .
4. $-3x=60-2x$ ; this simplifies to $-x=60$ , so $x=-60$ . However, this solution is extraneous because the absolute value of $2x-|60-2x|$ cannot be negative.
The sum of all of the solutions of $x$ is $20+60+12=\boxed{\textbf{(C)}\ 92}$

## Video Solution
https://youtu.be/vYXz4wStBUU?t=272
~IceMatrix
https://youtu.be/1DjO74VEr3E
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .