# 2013 AIME I Problem 2

## Problem

Find the number of five-digit positive integers, $n$ , that satisfy the following conditions:

## Solution 1
The number takes a form of $\overline{5xyz5}$ , in which $5|(x+y+z)$ . Let $x$ and $y$ be arbitrary digits. For each pair of $x,y$ , there are exactly two values of $z$ that satisfy the condition of $5|(x+y+z)$ . Therefore, the answer is $10\times10\times2=\boxed{200}$

## Solution 2 (casework)
We know the number will take the form $\overline{5xyz5}$ because of the first two conditions. The third condition means that $5|(x+y+z)$ , where $x,y,z$ are nonnegative integers less than $10$ . Let's split the problem into cases, where each case represents a possible sum of $x,y,z$ .
1. If $x+y+z=0$ , we only have $x=0,y=0,z=0$ , so only $1$ .
2. If $x+y+z=5$ , we use stars & bars. We have $5$ stars and $3-1=2$ bars, so this case has $7\choose{2}$ $= 21$ .
3. If $x+y+z=10$ , we use similar logic. We have $10$ stars and $2$ bars, so $12\choose{2}$ $= 66$ . However, $x,y,z$ must be less than $10$ . Three of our order pairs have $10: (10,0,0), (0,10,0), (0,0,10)$ . Therefore, this case has $66-3=63$ .
4. If $x+y+z=15$ , it gets more complicated. Using the same system as used previously would be too complicated. But remember that this case is equivalentto if we wanted to choose $x+y+z=12$ . We know this because you can take any ordered pair satisfying $x+y+z=15,$ subtract each variable from $9$ , and get an ordered pair satisfying $x+y+z=12$ . For example, take $(5,6,4)$ , which satisfies $x+y+z=15.$ Its corresponding ordered pair would be $(4,3,5)$ , which satisfies $x+y+z=12$ . Let's proceed to calculating. Applying stars and bars, we get $14\choose{2}$ $= 91$ , but we have to subtract the subcases including $10,11,$ or $12$ because $x,y,z$ must all be one-digit integers. There are $3$ cases with a $12$ , $6$ cases with an $11$ , and $3+6$ cases with a $10$ . So this case has $91-18=73$ .
5. If $x+y+z=20$ , we can just calculate the ways to get $x+y+z=7$ . Applying stars & bars, we get $9\choose{2}$ $= 36$ .
6. If $x+y+z=25$ , we can just calculate the ways to get $x+y+z=2.$ Applying stars & bars, we get $4\choose{2}$ $= 6$ .
Therefore, our answer is $1+21+63+73+36+6 = \boxed{200}$ .
Note: For case 4, the subcases that must be excluded are $(12,0,0), (11,1,0), (10,2,0), (10,1,1)$ and each of their respective permutations. Those $4$ ordered pairs have $3,6,6,3$ permutations respectively, which is why $18$ ordered pairs must be subtracted from $91$ .
~lprado

## Video Solution
https://www.youtube.com/watch?v=kz3ZX4PT-_0 ~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .