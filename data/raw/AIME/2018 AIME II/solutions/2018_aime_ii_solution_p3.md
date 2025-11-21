# 2018 AIME II Problem 3

## Problem

Find the sum of all positive integers $b < 1000$ such that the base- $b$ integer $36_{b}$ is a perfect square and the base- $b$ integer $27_{b}$ is a perfect cube.

## Solution 1
The first step is to convert $36_{b}$ and $27_{b}$ into base-10 numbers. Then, we can write \[36_{b} = 3b + 6\] and \[27_{b} = 2b + 7\] . It should also be noted that $8 \leq b < 1000$ .
Because there are less perfect cubes than perfect squares for the restriction we are given on $b$ , it is best to list out all the perfect cubes. Since the maximum $b$ can be is 1000 and $2$ • $1000 + 7 = 2007$ , we can list all the perfect cubes less than 2007.
Now, $2b + 7$ must be one of \[3^3, 4^3, ... , 12^3\] . However, $2b + 7$ will always be odd, so we can eliminate the cubes of the even numbers and change our list of potential cubes to \[3^3, 5^3, 7^3, 9^3\text{, and }11^3\] .
Because $3b + 6$ is a perfect square and is clearly divisible by 3, it must be divisible by 9, so $b + 2$ is divisible by 3. Thus the cube, which is \[2b + 7 = 2(b + 2) + 3\] , must also be divisible by 3. Therefore, the only cubes that $2b + 7$ could potentially be now are $3^3$ and $9^3$ .
We need to test both of these cubes to make sure $3b + 6$ is a perfect square.
$\textbf{Case 1:}$ If we set \[3^3 = 2b + 7\] so \[b = 10\] . If we plug this value of b into $3b + 6$ , the expression equals $36$ , which is indeed a perfect square.
$\textbf{Case 2:}$ If we set \[9^3 = 2b + 7\] so \[b = 361\] . If we plug this value of b into $3b + 6$ , the expression equals $1089$ , which is $33^2$ .
We have proven that both $b = 10$ and $b = 361$ are the only solutions, so \[10 + 361 = \boxed{371}\]

## Solution 2
The conditions are: \[3b+6 = n^2\] \[2b+7 = m^3\] We can see $n$ is multiple is 3, so let $n=3k$ , then $b= 3k^2-2$ . Substitute $b$ into second condition and we get $m^3=3(2k^2+1)$ . Now we know $m$ is both a multiple of 3 and odd. Also, $m$ must be smaller than 13 for $b$ to be smaller than 1000. So the only two possible values for $m$ are 3 and 9. Test and they both work. The final answer is $10 + 361 =$ $\boxed{371}$ . -Mathdummy

## Solution 3
As shown above, let \[3b+6 = n^2\] \[2b+7 = m^3\] such that \[6b+12=2n^2\] \[6b+21=3m^3\]
Subtracting the equations we have \[3m^3-2n^2=9 \implies 3m^3-2n^2-9=0.\]
We know that $m$ and $n$ both have to be integers, because then the base wouldn't be an integer. Furthermore, any integer solution $m$ must divide $9$ by the Rational Root Theorem.
We can instantly know $m \neq -9,-3,-1,1$ since those will have negative solutions.
When $m=3$ we have $n=6$ , so then $b=10$
When $m=9$ we have $n=33$ , so then $b=361$
Therefore, the sum of all possible values of $b$ is \[10+361=\boxed{371}.\]
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .