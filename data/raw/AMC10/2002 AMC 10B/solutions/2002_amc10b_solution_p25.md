# 2002 AMC 10B Problem 25

## Problem

When $15$ is appended to a list of integers, the mean is increased by $2$ . When $1$ is appended to the enlarged list, the mean of the enlarged list is decreased by $1$ . How many integers were in the original list?

$\mathrm{(A) \ } 4\qquad \mathrm{(B) \ } 5\qquad \mathrm{(C) \ } 6\qquad \mathrm{(D) \ } 7\qquad \mathrm{(E) \ } 8$

## Solution 1
Let $x$ be the sum of the integers and $y$ be the number of elements in the list. Then we get the equations $\dfrac{x+15}{y+1}=\dfrac{x}{y}+2$ and $\dfrac{x+15+1}{y+1+1}=\dfrac{x+16}{y+2}=\frac{x}{y}+2-1=\frac{x}{y}+1$ . With a lot of algebra, the solution is found to be $y= \boxed{\textbf{(A)}\ 4}$ .

## Solution 2
We let $n$ be the original number of elements in the set and we let $m$ be the original average of the terms of the original list. Then we have $mn$ is the sum of all the elements of the list. So we have two equations: \[mn+15=(m+2)(n+1)=mn+m+2n+2\] and \[mn+16=(m+1)(n+2)=mn+2m+n+2.\] Simplifying both equations and we get, \[13=m+2n\] \[14=2m+n\] Solving for $m$ and $n$ , we get $m=5$ and $n=\boxed{\textbf{(A)}4}$ .

## Solution 3
Warning: This solution will rarely ever work in any other case. However, seeing that you can so easily plug and chug in problem 25 it is funny to see this.
Plug and chug random numbers with the answer choices, starting with the choice of $4$ numbers. You see that if you have 4 5s and you add 15 to the set, the resulting mean will be 7; we can verify this with math \[\frac{5+5+5+5+15}{5}=7\] adding in 1 to the set you result in the mean to be 6. \[\frac{5+5+5+5+15+1}{6}=6\] Thus we conclude that 4 is the correct choice or $\boxed{\textbf{(A)}}$
Video solution by Canadamath https://www.youtube.com/watch?v=hYq8GgJ0it4

## Solution 4
Let $S$ be the sum of the numbers. Let $x$ be the number of integers, and the mean be $y$ . We have the equation $\frac{S}{x} = y$ . We also have $\frac{S+15}{x+1} = y+2$ and $\frac{S+16}{x+2} = y+1$ . From the first equation, we have $S = xy$ . We can multiply both sides by the denominators of the second and third equations to yield $S+15 = xy+2x+y+2$ and $S+16 = xy+x+2y+2$ . Since $S = xy$ , we can substitute that into the equations and subtract by $xy$ to get $15 = 2x+y+2$ or $13 = 2x+y$ . We also get $x+2y = 14$ , and adding the two equations up gives $3x+3y = 27$ , or $x+y = 9$ . Subtracting $x+y=9$ from $2x+y=13$ gives $x = 4$ and $y = 5$ .
We can check that this is the correct answer by having $4, 9, 6,$ and $1$ as our numbers. The sum is 20, and the mean is 5. Adding 15 gives that the sum is 35, and the number of integers is 5, so the mean is 2, an increase of 2. Adding 1 to the integers gives that the sum is 36, and the number of numbers is 6, for a mean of 6, a decrease of 1.
We can also prove that since the sum is 20, the number of integers is 4, and the mean is 5, we have $\frac{20}{4} = 5$ , which is true. The second equation gives $\frac{35}{5} = 7 = 5+2$ , which satisfies the condition. We also have $\frac{36}{6} = 6 = 7-1$ , which also satisfies the condition.
Therefore, since we correctly solved it and checked our work multiple ways, we can be confident that the answer is $\textbf{(A)}$ .

## Solution 5 (very similar to Solution 1)
Like in Solution 1, in the original list of numbers, we have $a$ terms which sum up to $b$ . Thus the mean of the original list of numbers is $\dfrac{b}{a}$ . With a bit of thinking we form an equation $\dfrac{b+15}{a+1}=\dfrac{b}{a}+2$ . In words this states we add 15 to total sum $b$ and because we add $1$ term to the total amount of terms $a$ , the ratio of this is the average of this new set which is formed by adding 15 to the old set and is equal to 2 more than the original average. Similarly we can form another equation $\dfrac{b+15+1}{a+1+1}=\dfrac{b}{a}+2-1$ , which is the relationship of the newest set's average to the original set's average. We add $1$ to both sides of the equation to get $\dfrac{b+16+(a+2)}{(a+2)}=\dfrac{b}{a}+2$ . And notice that we can set the two expressions equal to each other $\dfrac{b+16+(a+2)}{(a+2)}=\dfrac{b+15}{a+1}$ . And now we start to substitute values for a that correspond to the answer choices, we start by substituting $a=4$ . And we get $\dfrac{b+22}{(6)}=\dfrac{b+15}{5}$ , and $b=20$ . We find that this list with the terms summing up to $20$ and there are $4$ terms works. And thus our answer is $\textbf{(A)}$ . ~blankbox

## Solution 6 (one variable)
Notice if you append a number $a$ to a list with $b$ terms and the average changes by $c$ , then the original mean is \[a-c(b+1)\] .
Let the number of terms in the list be $y$ . Using the first statement that adding 15 makes the average go up 2, \[15-2(y+1)=13-2y\] is the mean of the list. Multiplying this by the number of terms in the list to get the sum of the terms in the list gives us \[y(13-2y)\] .
Using the second statement that after adding 15, we add 1 so that the average goes up 2 then goes down 1, meaning adding 16 will make the average go up 1. The sum of the terms plus 16, will result in the average plus 1 times the number of terms plus 2: \[y(13-2y)+16=(13-2y+1)(y+2)=(14-2y)(y+2)\]
Expanding this gives us: \[-2y^2+13y+16=-2y^2+10y+28\] which then simplifies to $3y=12$ , or $y=4$ and the answer is $\textbf{(A)}$ . ~penguin_pro

## Video Solution
https://www.youtube.com/watch?v=u8zi0QikJK0 ~David
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .